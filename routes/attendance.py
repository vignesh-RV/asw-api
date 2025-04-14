from datetime import datetime

from flask import Blueprint, request, jsonify
from models import Users, Parent, ParentSchema, Attendance
from extension.extensions import db
from routes.students import RFID

attendance_bp = Blueprint('attendance_bp', __name__)
parent_schema = ParentSchema(many=True)


@attendance_bp.route('/range', methods=['POST'])
def get_attendance_by_range():
    data = request.get_json()

    # Extracting date range from request body
    start_date_str = data.get('startDate')
    end_date_str = data.get('endDate')

    if not start_date_str or not end_date_str:
        return jsonify({"error": "Both start_date and end_date are required"}), 400

    try:
        # Convert from ISO 8601 format (UTC) to datetime object
        start_date = datetime.fromisoformat(start_date_str.replace("Z", ""))
        end_date = datetime.fromisoformat(end_date_str.replace("Z", ""))
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO 8601 (e.g., 2025-04-30T23:59:59.000Z)"}), 400

    # Query filtering by date range
    records = Attendance.query.filter(
        Attendance.created_date >= start_date,
        Attendance.created_date <= end_date
    ).all()

    return jsonify([record.to_dict() for record in records])


@attendance_bp.route('/', methods=['POST'])
def post():
    """Create a new attendance record."""
    data = request.get_json()
    print(data)
    rfid_data = RFID.query.filter_by(uuid=data.get('rfid_uuid')).first()
    if not rfid_data:
        return jsonify({"status": "error", "data": "Invalid RFID.."}), 401

    user_data = Users.query.filter_by(user_id=rfid_data.holder_id, face_id=data.get('face_id')).first()
    if not user_data:
        return jsonify({"status": "error", "data":  "Face ID is not matching.."}), 401
    if data.get('thump_id') != '' and user_data.thump_id != data.get('thump_id'):
        return jsonify({"status": "error", "data":  "Thump ID is not matching.."}), 401

    new_record = Attendance(
        user_id=user_data.user_id,
        punch_type=data.get("punch_type", "IN")
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Attendance record added!", "record": new_record.to_dict()})


@attendance_bp.route('/', methods=['PUT'])
def put(attendance_id):
    """Update an existing attendance record."""
    attendance = Attendance.query.get_or_404(attendance_id)
    data = request.get_json()
    attendance.punch_type = data.get("punch_type", attendance.punch_type)
    db.session.commit()
    return jsonify({"message": "Attendance record updated!", "record": attendance.to_dict()})


@attendance_bp.route('/<int:attendance_id>', methods=['DELETE'])
def delete(attendance_id):
    """Delete an attendance record."""
    attendance = Attendance.query.get_or_404(attendance_id)
    db.session.delete(attendance)
    db.session.commit()
    return jsonify({"message": "Attendance record deleted!"})

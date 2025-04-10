from datetime import datetime

from flask import Blueprint, request, jsonify
from extension.extensions import db, ma


student_bp = Blueprint('student_bp', __name__)

# Student Model
class RFID(db.Model):
    __tablename__ = 'rfids'

    rf_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    holder_id = db.Column(db.BigInteger, nullable=False)
    locked = db.Column(db.Boolean, nullable=False, default=False)
    balance = db.Column(db.BigInteger, nullable=False, default=0)
    max_limit = db.Column(db.BigInteger, nullable=False, default=0)
    uuid = db.Column(db.String(100), nullable=False, default=0)
    created_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    created_by = db.Column(db.BigInteger, nullable=False, default=-1)
    last_modified_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_modified_by = db.Column(db.BigInteger, nullable=False, default=-1)

    def __init__(self, holder_id, balance=0, max_limit=0, created_by=-1, last_modified_by=-1):
        self.holder_id = holder_id
        self.balance = balance
        self.max_limit = max_limit
        self.created_by = created_by
        self.last_modified_by = last_modified_by


# Schema for JSON Serialization
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RFID


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# Create a new student
@student_bp.route('/create_rfid', methods=['POST'])
def create_rfid():
    data = request.json
    new_student = RFID(holder_id=data['student_id'], balance=data.get('balance', 0.0))
    db.session.add(new_student)
    db.session.commit()
    return student_schema.jsonify(new_student)


# Get all students
@student_bp.route('/students', methods=['GET'])
def get_students():
    all_students = RFID.query.all()
    return students_schema.jsonify(all_students)


# Get a single student by RFID
@student_bp.route('/students/<rfid>', methods=['GET'])
def get_student(rfid):
    student = RFID.query.filter_by(rfid=rfid).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404
    return student_schema.jsonify(student)


# Get a single student by user id
@student_bp.route('/rfid/holder/<holder_id>', methods=['GET'])
def get_rfid_by_student(holder_id):
    student = RFID.query.filter_by(holder_id=holder_id).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404
    return student_schema.jsonify(student)


# Update a student's details
@student_bp.route('/students/<rfid>', methods=['PUT'])
def update_student(rfid):
    student = RFID.query.filter_by(rfid=rfid).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.json
    student.name = data.get('name', student.name)
    db.session.commit()
    return student_schema.jsonify(student)


@student_bp.route('/recharge/<rfid>', methods=['PUT'])
def recharge(rfid):
    student = RFID.query.filter_by(rf_id=rfid).first()
    if not student:
        return jsonify({"message": "Student card data is not found"}), 404

    data = request.json
    student.balance += data.get('amount', student.balance)
    db.session.commit()
    return student_schema.jsonify(student)

@student_bp.route('/limit/<rfid>', methods=['PUT'])
def update_limits(rfid):
    student = RFID.query.filter_by(rf_id=rfid).first()
    if not student:
        return jsonify({"message": "Student card data is not found"}), 404

    data = request.json
    student.max_limit = data.get('max_limit')
    db.session.commit()
    return student_schema.jsonify(student)

@student_bp.route('/lock/<rfid>', methods=['PUT'])
def lock_card(rfid):
    student = RFID.query.filter_by(rf_id=rfid).first()
    if not student:
        return jsonify({"message": "Student card data is not found"}), 404

    data = request.json
    student.locked = data.get('locked')
    db.session.commit()
    return student_schema.jsonify(student)

# Delete a student
@student_bp.route('/students/<rfid>', methods=['DELETE'])
def delete_student(rfid):
    student = RFID.query.filter_by(rfid=rfid).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"})


# Add money to RFID card
@student_bp.route('/students/<rfid>/add_money', methods=['POST'])
def add_money(rfid):
    student = RFID.query.filter_by(rfid=rfid).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404

    amount = request.json.get('amount', 0)
    if amount <= 0:
        return jsonify({"message": "Invalid amount"}), 400

    student.balance += amount
    db.session.commit()
    return student_schema.jsonify(student)


# Deduct money for canteen/library payments
@student_bp.route('/students/<rfid>/pay', methods=['POST'])
def make_payment(rfid):
    student = RFID.query.filter_by(rfid=rfid).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404

    amount = request.json.get('amount', 0)
    if amount <= 0:
        return jsonify({"message": "Invalid amount"}), 400
    if student.balance < amount:
        return jsonify({"message": "Insufficient balance"}), 400

    student.balance -= amount
    db.session.commit()
    return student_schema.jsonify(student)


# Mark attendance
@student_bp.route('/students/<rfid>/attendance', methods=['POST'])
def mark_attendance(rfid):
    student = RFID.query.filter_by(rfid=rfid).first()
    if not student:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({"message": f"Attendance marked for {student.name}"})

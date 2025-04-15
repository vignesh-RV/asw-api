import json

from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from sqlalchemy import desc

from models import db, Payment, Users  # Import your model
from routes.students import RFID

payments_bp = Blueprint('payments_bp', __name__)

# Create a payment
@payments_bp.route('/', methods=['POST'])
def create_payment():
    data = request.get_json()
    print(data)
    if not data.get('amount'):
        return jsonify({"error": "Amount are required"}), 400

    rfid_data = RFID.query.filter_by(uuid=data.get('rfid_uuid')).first()
    if not rfid_data:
        return jsonify({"message": "Invalid RFID.."}), 401
    user_data = Users.query.filter_by(user_id=rfid_data.holder_id, face_id=data.get('face_id')).first()
    if not user_data:
        return jsonify({"message": "Face ID is not matching.."}), 401
    if data.get('thump_id') != '' and user_data.thump_id != data.get('thump_id'):
        return jsonify({"message": "Thump ID is not matching.."}), 401

    # validate student available balance
    user_id = user_data.user_id
    cardData = rfid_data

    if cardData.balance < data['amount']:
        return jsonify({"status": "error", "data": "Insufficient balance.."}), 500

    if cardData.locked:
        return jsonify({"status": "error", "data": "Card is Locked.."}), 500

    new_payment = Payment(
        user_id=user_id,
        transaction_type=data.get('transaction_type', 'TUITION'),
        amount=data['amount'],
        location= json.dumps(data['location']),
        object_id=data['object_id']
    )
    db.session.add(new_payment)
    db.session.commit()

    # adjust the card balance
    rfid = RFID.query.filter_by(rf_id=cardData.rf_id).first()
    rfid.balance -= data['amount']
    db.session.commit()

    return jsonify(new_payment.to_dict()), 201

# Get all payments
@payments_bp.route('/', methods=['GET'])
def get_all_payments():
    payments = Payment.query.order_by(desc(Payment.created_date)).all()
    return jsonify([payment.to_dict() for payment in payments])

# Get a payment by ID
@payments_bp.route('/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return jsonify(payment.to_dict())


# Get all payments for a specific user_id
@payments_bp.route('/user/<int:user_id>', methods=['GET'])
def get_payments_by_user(user_id):
    payments = Payment.query.order_by(desc(Payment.created_date)).filter_by(user_id=user_id).all()

    # if not payments:
    #     return jsonify({"message": "No payments found for this user"}), 404

    return jsonify([payment.to_dict() for payment in payments])


# Update a payment
@payments_bp.route('/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    data = request.get_json()

    payment.transaction_type = data.get('transaction_type', payment.transaction_type)
    payment.amount = data.get('amount', payment.amount)

    db.session.commit()
    return jsonify(payment.to_dict())

# Delete a payment
@payments_bp.route('/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({"message": "Payment deleted successfully"})

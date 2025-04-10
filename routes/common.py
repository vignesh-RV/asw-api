import os

from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from twilio.rest import Client

from models import db, PlacementFee, ArrearFee, RevaluationFee  # Import the model
# Load environment variables from .env file
load_dotenv()
common_bp = Blueprint('common_bp', __name__)

# Get all placement fees
@common_bp.route('/placement_fees', methods=['GET'])
def get_all_placement_fees():
    placement_fees = PlacementFee.query.all()
    return jsonify([fee.to_dict() for fee in placement_fees])


@common_bp.route('/arrear_fees', methods=['GET'])
def get_all_arrear_fees():
    placement_fees = ArrearFee.query.all()
    return jsonify([fee.to_dict() for fee in placement_fees])


@common_bp.route('/revaluation_fees', methods=['GET'])
def get_all_revaluation_fees():
    revaluation_fees = RevaluationFee.query.all()
    return jsonify([fee.to_dict() for fee in revaluation_fees])


@common_bp.route('/trigger_otp', methods=['POST'])
def trigger_otp():
    data = request.json
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    verification = client.verify \
        .v2 \
        .services( os.getenv("TWILIO_VERIFY_SERVICE_SID") ) \
        .verifications \
        .create(to='+917397719755', channel='sms')

    print(verification.sid)
    return jsonify({"status": "success", "sid": verification.sid}), 200

@common_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    data = request.json
    try:
        verification_check = client.verify \
            .v2 \
            .services( os.getenv("TWILIO_VERIFY_SERVICE_SID") ) \
            .verification_checks \
            .create(to='+917397719755', code=f'{data.get("code")}')

        print(verification_check.status)
        return jsonify({"status": verification_check.status}), 200
    except Exception as e:
        print(e)
        return jsonify({"status": "FAILED"}), 500
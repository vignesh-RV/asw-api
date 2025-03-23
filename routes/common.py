from flask import Blueprint, jsonify
from models import db, PlacementFee, ArrearFee, RevaluationFee  # Import the model

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
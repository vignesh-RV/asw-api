import json
import os
from datetime import datetime

import numpy as np
from deepface import DeepFace
from flask import Blueprint, request, jsonify
from models import Users,Parent, ParentSchema
from extension.extensions import db
import base64
from sqlalchemy import text

user_bp = Blueprint('user_bp', __name__)
parent_schema = ParentSchema(many=True)

@user_bp.route('/', methods=['POST'])
def create_user():
    print("Request received to create student")
    data = request.get_json()
    new_user = Users(**data)
    new_user.password =encode_base64(new_user.password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully", "user_id": new_user.user_id}), 201

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get_or_404(user_id)
    user_data = {column.name: getattr(user, column.name) for column in Users.__table__.columns if
                 column.name != 'password'}
    return jsonify(user_data)


@user_bp.route('/list', methods=['GET'])
def get_users():
    all_users = Users.query.with_entities(Users.user_id, Users.reg_no, Users.user_name,Users.user_type, Users.course, Users.batch, Users.section_name, Users.semester, Users.current_year, Users.course_duration_in_years, Users.created_date).all()
    user_list = [u._asdict() for u in all_users]
    return jsonify(user_list)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Users.query.get_or_404(user_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({"message": "User updated successfully"})

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})


@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        reg_no = data.get('reg_no')
        password = data.get('password')
        user_type = data.get('user_type')

        if not reg_no or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        query = text("SELECT user_id, password, user_type FROM users WHERE reg_no = :reg_no")
        result = db.session.execute(query, {"reg_no": reg_no})
        user_row = result.fetchone()
        if not user_row:
            return jsonify({'error': 'Invalid registration number..'}), 401

        if encode_base64(password) != user_row[1]:
            return jsonify({'error': 'Incorrect password..'}), 401
        if user_type != user_row[2] and user_row[2] == 'STAFF':
            return jsonify({'error': 'Invalid user type..'}), 401
        return get_user(int(user_row[0]))

    except db.connector.Error as e:
        return jsonify({'error': 'Invalid registration number or password'}), 401


parent_schema = ParentSchema(many=True)

# GET API to fetch parents by student_id
@user_bp.route('/parents/<int:student_id>', methods=['GET'])
def get_parents_by_student(student_id):
    parents = Parent.query.filter_by(student_user_id=student_id).all()
    return jsonify(parent_schema.dump(parents))


@user_bp.route('/parents', methods=['POST'])
def store_parent():
    try:
        data = request.json
        parents = data

        if not parents:
            return jsonify({"error": "No parent data provided"}), 400

        parent_objects = []
        for parent in parents:
            existing_parent = Parent.query.filter_by(parent_id=parent.get('parent_id')).first()
            new_parent = existing_parent if existing_parent is not None else Parent()

            # Get model columns dynamically
            parent_columns = Parent.__table__.columns.keys()

            for column in parent_columns:
                if column != "parent_id":  # Skip auto-increment primary key
                    setattr(new_parent, column, parent.get(column))  # Set value dynamically
                elif parent.get(column) is not None:
                    setattr(new_parent, column, parent.get(column))
            new_parent.created_date = new_parent.created_date or datetime.utcnow()
            new_parent.created_by = new_parent.created_by or -1
            new_parent.last_modified_date = datetime.utcnow()
            new_parent.last_modified_by = parent.get('student_user_id')


            parent_objects.append(new_parent)

        db.session.add_all(parent_objects)
        db.session.commit()

        return jsonify({"message": "Parents added successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def encode_base64(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')



# Function to encode a face
def encode_face(image_path):
    return None


@user_bp.route('/verify', methods=['POST'])
def verify():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = os.path.join("images", "uploaded_image.jpg")
    file.save(filename)

    # Compare with known image (this should be a predefined stored image)
    known_image_path = os.path.join("images", "passport-size.PNG")  # Change this path as needed

    try:
        result = DeepFace.verify(filename, known_image_path)
        match = result["verified"]
        return jsonify({"match": match, "message": "Match Found" if match else "No Match"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
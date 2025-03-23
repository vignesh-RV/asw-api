from extension.extensions import db, ma
from datetime import datetime

class Users(db.Model):
    user_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(100), nullable=False, default='STUDENT')
    gender = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    dob = db.Column(db.Date, nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    religion = db.Column(db.String(100), nullable=True)
    caste = db.Column(db.String(100), nullable=True)
    mother_tongue = db.Column(db.String(100), nullable=True)
    native_place = db.Column(db.String(100), nullable=True)
    mobile_no = db.Column(db.BigInteger, nullable=False, unique=True)
    aadhaar = db.Column(db.BigInteger, nullable=True, unique=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    first_graduate = db.Column(db.Boolean, nullable=False, default=False)
    reg_no = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_by = db.Column(db.BigInteger, nullable=False, default=-1)
    last_modified_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_modified_by = db.Column(db.BigInteger, nullable=False, default=-1)
    batch = db.Column(db.String(100), nullable=True)
    semester = db.Column(db.BigInteger, nullable=True, default=1)
    course = db.Column(db.String(100), nullable=True)
    school = db.Column(db.String(100), nullable=True)
    current_year = db.Column(db.BigInteger, nullable=True, default=1)
    section_name = db.Column(db.String(100), nullable=True)
    blood_group = db.Column(db.String(100), nullable=True)
    course_duration_in_years = db.Column(db.BigInteger, nullable=True, default=2)
    course_fees = db.Column(db.BigInteger, nullable=True, default=10000)
    profile_image = db.Column(db.Text, nullable=True)

class Parent(db.Model):
    __tablename__ = 'parents'

    parent_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    parent_type = db.Column(db.String(100), nullable=False, default='FATHER')
    full_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)
    annual_income = db.Column(db.BigInteger, nullable=False)
    profile_image = db.Column(db.Text, nullable=True)
    occupation = db.Column(db.String(100), nullable=True)
    designation = db.Column(db.String(100), nullable=True)
    aadhaar_no = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    student_user_id = db.Column(db.BigInteger, nullable=False)
    created_date = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    created_by = db.Column(db.BigInteger, nullable=False, default=-1)
    last_modified_date = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(),
                                   onupdate=db.func.current_timestamp())
    last_modified_by = db.Column(db.BigInteger, nullable=False, default=-1)


# Schema for serialization
class ParentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Parent
        load_instance = True


class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    punch_type = db.Column(db.String(100), default='RFID')
    created_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Attendance id={self.id}, user_id={self.user_id}, punch_type={self.punch_type}, created_date={self.created_date}>"

    def to_dict(self):
        """Convert model to dictionary for JSON response."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "punch_type": self.punch_type,
            "created_date": self.created_date.strftime('%Y-%m-%d %H:%M:%S')
        }

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    transaction_type = db.Column(db.String(100), nullable=False, default='FEES')
    amount = db.Column(db.BigInteger, nullable=False, default=0)
    object_id = db.Column(db.BigInteger, nullable=True, default=-1)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "object_id": self.object_id,
            "created_date": self.created_date.isoformat()
        }


class PlacementFee(db.Model):
    __tablename__ = 'placement_fees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exam_name = db.Column(db.String(100), nullable=False)
    fees = db.Column(db.BigInteger, nullable=False, default=0)
    due_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "exam_name": self.exam_name,
            "fees": self.fees,
            "due_date": self.due_date.isoformat()
        }

class ArrearFee(db.Model):
    __tablename__ = 'arrear_fees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(100), nullable=False)
    fees = db.Column(db.BigInteger, nullable=False, default=0)
    due_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "fees": self.fees,
            "due_date": self.due_date.isoformat()
        }


class RevaluationFee(db.Model):
    __tablename__ = 'revaluation_fees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(100), nullable=False)
    fees = db.Column(db.BigInteger, nullable=False, default=0)
    due_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "fees": self.fees,
            "due_date": self.due_date.isoformat()
        }
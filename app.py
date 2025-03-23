from flask import Flask
from extension.extensions import db, ma
from routes.attendance import attendance_bp
from routes.common import common_bp
from routes.payments import payments_bp
from routes.users import user_bp
from routes.students import student_bp
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
ma.init_app(app)

# Allow CORS for all routes
CORS(app, origins=["http://localhost:4200"])

# Test connection
with app.app_context():
    try:
        with db.engine.connect() as connection:
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(student_bp, url_prefix='/students')
app.register_blueprint(attendance_bp, url_prefix='/attendance')
app.register_blueprint(payments_bp, url_prefix='/payments')
app.register_blueprint(common_bp, url_prefix='/common')

if __name__ == '__main__':
    app.run(debug=True)
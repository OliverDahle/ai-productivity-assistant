from . import db
from flask_login import UserMixin

# Using the Flask-SQLAlchemy to define models that can interact with the database

# Defining the User model with UserMixin to help with methods for Flask-Login; authentication and login status
# The columns should be self explanatory
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    life_situation = db.Column(db.String(100))
    schema_id = db.Column(db.Integer, db.ForeignKey('schema.id'))

class Schema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # The predefined layout, not changeable by the user
    schema_layout = db.Column(db.Text)
    # The personal preferences of the users, this is changeable
    schema_personal = db.Column(db.Text)
    # One to many relationship in case multiple users want the same schema
    users = db.relationship('User', backref='schema', lazy=True)

# The output of the AI-generated plan
class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tekstformat = db.Column(db.Text)

# Links the users to their plans by way of ids, also saves the plans time of creation
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    plan_name = db.Column(db.String(200))
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

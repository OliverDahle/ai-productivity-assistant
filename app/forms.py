from flask_wtf import FlaskForm
# Importing different form field types
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField
# Importing different input validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

# For when a new user signs up to the web app
# I use different validators from the wtforms library to ensure valid input
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[EqualTo('password')])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=150)])
    gender = SelectField('Gender', choices=[('Male','Male'), ('Female','Female'), ('Other','Other')], validators=[DataRequired()])
    life_situation = SelectField('Life Situation', choices=[('Student','Student'), ('Employed','Employed'), ('Unemployed','Unemployed'), ('Other','Other')], validators=[DataRequired()])
    submit = SubmitField('Register')

# Login form, not much to add, pretty straight forward
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Input for creating a plan
class PlanInputForm(FlaskForm):
    time_available = StringField('Time Available', validators=[DataRequired()])
    tasks = TextAreaField('Tasks', validators=[DataRequired()])
    submit = SubmitField('Generate Plan')

# For updating the personal preferences
class SchemaForm(FlaskForm):
    personal_schema = TextAreaField('Personal Preferences', validators=[DataRequired()])
    submit = SubmitField('Update Personal Preferences')

# For updating the profile
class ProfileForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=150)])
    gender = SelectField('Gender', choices=[('Male','Male'), ('Female','Female'), ('Other','Other')], validators=[DataRequired()])
    life_situation = SelectField('Life Situation', choices=[('Student','Student'), ('Employed','Employed'), ('Unemployed','Unemployed'), ('Other','Other')], validators=[DataRequired()])
    submit = SubmitField('Update Profile')

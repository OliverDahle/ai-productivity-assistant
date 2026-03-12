from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
# Local imports:
from .models import User
from .forms import RegisterForm, LoginForm, ProfileForm
from . import db, login_manager

# Creates a Blueprint called auth to group all routes locally
bp = Blueprint('auth', __name__)

# Defining how to load a user from a session ID, this keeps users logged in between requests
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register a user
@bp.route('/register', methods=['GET', 'POST'])
def register():
    # On GET displays the registration form
    form = RegisterForm()
    # On POST Flask-WTF validates all fields
    if form.validate_on_submit():
        # Hashes the password for storing
        hashed_pw = generate_password_hash(form.password.data)
        # Creates and saves the new user in the database
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw,
            age=form.age.data,
            gender=form.gender.data,
            life_situation=form.life_situation.data
        )
        db.session.add(new_user)
        db.session.commit()
        # When registered the user will be logged in and redirected to the home page
        login_user(new_user)
        flash('Registration successful. You are now logged in.')
        return redirect(url_for('routes.home'))
    # GET
    return render_template('register.html', form=form)

# Logging in a user
# Same logic as register
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Finds the user in the database
        user = User.query.filter_by(username=form.username.data).first()
        # If the user exists and the user's password matches the input, the user is logged in and sent to home page
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('routes.home'))
        # Else flash error message
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)

# Logs out user and redirects to login page
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('auth.login'))

# Loads the profile form pre-filled with the user information
@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.age = form.age.data
        current_user.gender = form.gender.data
        current_user.life_situation = form.life_situation.data
        db.session.commit()
        flash('The profile has been updated')
        return redirect(url_for('auth.profile'))
    # Returns the pre-filled form if it is not yet submitted or invalid input
    return render_template('profile.html', form=form)

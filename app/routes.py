from flask import Blueprint, render_template
from flask_login import login_required

# Creates a Blueprint called routes to group all routes locally
bp = Blueprint('routes', __name__)

# When this route is called, render home.html, login is required
@bp.route('/')
@login_required
def home():
    return render_template('home.html')

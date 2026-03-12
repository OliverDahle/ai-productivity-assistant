from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os

# Loading the environment variables from my .env file
load_dotenv()

# Global extensions for my app
# I create these now and initialize later in the app, as it is best practice
db = SQLAlchemy()                   # Interacts with my database by using Python classes
login_manager = LoginManager()      # This handles login sessions and redirects
csrf = CSRFProtect()                # Secures all forms from CSRF attacks, this is indirectly used in all Flask-WTF form
migrate = Migrate()                 # Handles database schema changes via Alembic

# Creating the app object
def create_app():
    app = Flask(__name__)

    # Loading the secret key and sets the database url to my local file-based database
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'

    # Initializes the Flask Extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    # Redirect to login page if not logged in
    login_manager.login_view = 'auth.login'

    # Registers all Blueprints (the route modules)
    from . import routes, auth, planner
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(planner.bp)

    return app

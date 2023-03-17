from flask import Flask
from flask_migrate import Migrate
from .auth.routes import auth

app = Flask(__name__)

# login_manager = LoginManager(app)

# login_manager.login_view ='auth.loginPage'

app.register_blueprint(auth)

from . import routes


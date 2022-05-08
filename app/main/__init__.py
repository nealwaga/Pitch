from flask import Blueprint, Flask

main = Blueprint ('main', __name__)

from . import views,error
#from flask_login import LoginManager

#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'auth.login'
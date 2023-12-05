from flask import Blueprint
from src.controllers.auth import profile, sing_up, login, logout

auth_blueprint = Blueprint('auth', __name__)


auth_blueprint.route("/profile")(profile)
auth_blueprint.route('/sing_up', methods=["GET", "POST"])(sing_up)
auth_blueprint.route("/login", methods=["GET", "POST"])(login)
auth_blueprint.route("/logout")(logout)

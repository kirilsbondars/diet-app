from flask import Blueprint
from flask_login import login_required

from controllers.auth import profile, sing_up, login, logout

auth_blueprint = Blueprint('auth', __name__)

auth_blueprint.route("/", methods=["GET", "POST"])(login)
auth_blueprint.route("/profile", methods=["GET", "POST"])(login_required(profile))
auth_blueprint.route('/sing_up', methods=["GET", "POST"])(sing_up)
auth_blueprint.route("/logout")(logout)

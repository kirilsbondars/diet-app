from flask import Blueprint, redirect, url_for
from flask_login import login_required, current_user

from controllers.auth import profile, sing_up, login, logout

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route("/", methods=["GET", "POST"])
def start_page():
    if current_user.is_authenticated:
        return redirect(url_for('menu.create_menu_view'))
    else:
        return login()

auth_blueprint.route("/", methods=["GET", "POST"])(login)
auth_blueprint.route("/profile", methods=["GET", "POST"])(login_required(profile))
auth_blueprint.route('/sing_up', methods=["GET", "POST"])(sing_up)
auth_blueprint.route("/logout")(logout)

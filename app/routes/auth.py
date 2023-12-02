from flask import Blueprint

from app.controlers.auth import sing_up, login, logout

auth = Blueprint('auth', __name__)

auth.route('/sing-up', methods=["GET", "POST"])(sing_up)
auth.route("/", methods=["GET", "POST"])(login)
auth.route("/logout")(logout)

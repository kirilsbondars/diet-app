from flask import Blueprint
from src.controllers.menu import create_menu
from src.controllers.history import history
from flask_login import login_required

menu_blueprint = Blueprint('menu', __name__)

menu_blueprint.route('/menu', methods=['GET'])(login_required(create_menu))
menu_blueprint.route('/history', methods=['GET'])(login_required(history))

from flask import Blueprint
from src.controllers.menu import create_menu
from src.controllers.history import history

menu_blueprint = Blueprint('menu', __name__)

menu_blueprint.route('/menu', methods=['GET'])(create_menu)
menu_blueprint.route('/history', methods=['GET'])(history)

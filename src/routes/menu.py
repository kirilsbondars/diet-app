from flask import Blueprint
from flask_login import login_required
from src.controllers.menu import create_menu_view
from src.controllers.history import history

menu_blueprint = Blueprint('menu', __name__)

menu_blueprint.route('/menu', methods=['GET', 'POST'])(login_required(create_menu_view))
menu_blueprint.route('/history', methods=['GET'])(login_required(history))

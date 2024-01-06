from flask import Blueprint
from flask_login import login_required

from controllers.menu import create_menu_view
from controllers.history import history

menu_blueprint = Blueprint('menu', __name__)

menu_blueprint.route('/create-menu', methods=['GET', 'POST'])(login_required(create_menu_view))
menu_blueprint.route('/history', methods=['GET'])(login_required(history))

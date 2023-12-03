from flask import Blueprint
from src.controllers.menu import create_menu, create_menu_date
from src.controllers.recipe import recipe
from src.controllers.blacklist import blacklist
from src.controllers.history import history

menu_blueprint = Blueprint('menu', __name__)

menu_blueprint.route('/create-menu', methods=['GET'])(create_menu)
menu_blueprint.route('/create-menu/<date>', methods=['GET'])(create_menu_date)
menu_blueprint.route('/recipe/<recipe_id>', methods=['GET'])(recipe)
menu_blueprint.route('/blacklist', methods=['GET'])(blacklist)
menu_blueprint.route('/history', methods=['GET'])(history)

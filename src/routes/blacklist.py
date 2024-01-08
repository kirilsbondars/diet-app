from flask import Blueprint
from flask_login import login_required

from controllers.blacklist import view, add, remove

blacklist_blueprint = Blueprint('blacklist', __name__, url_prefix='/blacklist')

blacklist_blueprint.route('/', methods=['GET'])(login_required(view))
blacklist_blueprint.route('/add/<meal_id>/<history_date>', methods=['GET'])(login_required(add))
blacklist_blueprint.route('/remove/<meal_id>/<return_page>/<history_date>', methods=['GET'])(login_required(remove))

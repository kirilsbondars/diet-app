from flask import Blueprint

from controllers.index import render_page_index

index_blueprint = Blueprint('index', __name__)

index_blueprint.route('/index', methods=['GET'])(render_page_index)

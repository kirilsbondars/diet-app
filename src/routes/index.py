from flask import Blueprint
from src.controllers.index import render_page_index

index_blueprint = Blueprint('blueprint', __name__)

index_blueprint.route('/', methods=['GET'])(render_page_index)

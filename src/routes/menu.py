from flask import Blueprint
from src.controllers.menu import index

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)

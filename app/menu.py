from flask import Blueprint, render_template
from flask_login import login_required

menu = Blueprint('menu', __name__)


@menu.route('/create')
@login_required
def view():
    return render_template("menu/create.html")
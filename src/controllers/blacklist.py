from flask import render_template
from src.models.models import db


def blacklist():
    return render_template('menu/blacklist.html')


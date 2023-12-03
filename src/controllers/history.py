from flask import render_template
from src.models.models import db


def history():
    return render_template('menu/history.html')


from flask import render_template
from src.models.models import db, User


def render_page_index():
    return render_template('index.html')

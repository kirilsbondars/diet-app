from flask import render_template
from src.models.models import db


def create_menu():
    return render_template('menu/create-menu.html')


def create_menu_date(date):
    return render_template('menu/create-menu-date.html', date=date)

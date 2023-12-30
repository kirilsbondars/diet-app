from flask import render_template
from flask_login import current_user
from src.models.models import meal_blacklist, Meal
from src.models.models import db


def blacklist():
    blacklisted_meals = (db.session.query(Meal))
    return render_template('menu/blacklist.html', meals=blacklisted_meals)

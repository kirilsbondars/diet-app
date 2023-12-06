from flask import render_template
from src.models.models import db, User


def render_page_index():

    user = User.query.first()
    meals = user.meals
    for meal in meals:
        print(meal.name)

    return render_template('index.html')

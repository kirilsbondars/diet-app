from flask import render_template
from src.models.models import db


def recipe(recipe_id):
    return render_template('menu/recipe.html', recipe_id=recipe_id)

from flask import render_template
from src.models.models import db, User, user_meal, Meal
from sqlalchemy import insert
from datetime import datetime
from flask_login import current_user

from src.controllers.menu import create_one_day_menu

from src.models.models import Meal, db, user_meal
from datetime import date


def render_page_index():
    #create_one_day_menu()
    # user_meal_record1 = insert(user_meal).values(user_id=current_user.id, meal_id=1, date=datetime.now(),
    #                                              mealtime='Breakfast', portion=200)
    # user_meal_record2 = insert(user_meal).values(user_id=current_user.id, meal_id=2, date=datetime.now(),
    #                                              mealtime='Breakfast', portion=200)
    # user_meal_record3 = insert(user_meal).values(user_id=current_user.id, meal_id=3, date=datetime.now(),
    #                                              mealtime='Breakfast', portion=200)
    # user_meal_record4 = insert(user_meal).values(user_id=current_user.id, meal_id=4, date=datetime.now(),
    #                                              mealtime='Lunch', portion=200)
    #
    # db.session.execute(user_meal_record1)
    # db.session.execute(user_meal_record2)
    # db.session.execute(user_meal_record3)
    # db.session.execute(user_meal_record4)
    # db.session.commit()

    # Get today's date
    today = date.today()

    # Query for meals with user id = 1 and date = today
    # Query for meals with user id = 1 and date = today
    user_meals = db.session.query(Meal.name, user_meal.c.portion, Meal.calories, Meal.proteins, Meal.fats,
                                  Meal.carbohydrates).join(
        user_meal, Meal.id == user_meal.c.meal_id
    ).filter(
        user_meal.c.user_id == 1,
        user_meal.c.date == today
    ).all()

    # Now `user_meals` is a list of tuples with each tuple containing the meal name, portion, and nutrients for meals with user id = 1 and date = today
    for meal in user_meals:
        print(meal)
        # meal_name, portion, calories, proteins, fats, carbohydrates = meal
        # portion = float(portion)
        # print(f"Meal Name: {meal_name}, Portion: {portion}")
        # print(
        #     f"Calories: {float(calories) * portion / 100}, Proteins: {float(proteins) * portion / 100}, Fats: {float(fats) * portion / 100}, Carbohydrates: {float(carbohydrates) * portion / 100}")
    return render_template('index.html')

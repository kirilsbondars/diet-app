from flask import render_template
from src.models.models import db, User, user_meal
from sqlalchemy import insert
from datetime import datetime


def render_page_index():
    user = User.query.first()

    user_meal_record1 = insert(user_meal).values(user_id=user.id, meal_id=1, date=datetime.now(),
                                                          mealtime='Breakfast', portion=200)
    user_meal_record2 = insert(user_meal).values(user_id=user.id, meal_id=2, date=datetime.now(),
                                                          mealtime='Breakfast', portion=200)
    user_meal_record3 = insert(user_meal).values(user_id=user.id, meal_id=3, date=datetime.now(),
                                                          mealtime='Breakfast', portion=200)
    user_meal_record4 = insert(user_meal).values(user_id=user.id, meal_id=4, date=datetime.now(),
                                                          mealtime='Lunch', portion=200)

    db.session.execute(user_meal_record1)
    db.session.execute(user_meal_record2)
    db.session.execute(user_meal_record3)
    db.session.execute(user_meal_record4)
    db.session.commit()

    return render_template('index.html')

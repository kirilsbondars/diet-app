from flask import render_template, session, Flask, redirect, url_for, Blueprint, request
from flask_login import current_user
from src.models.models import db, User, Meal, user_meal
from datetime import datetime, timedelta


def history():
    date_str = request.args.get('date')
    if date_str is None:
        date = datetime.today().date()
    else:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            today_str = datetime.today().date()
            return redirect(url_for('menu.history', date=today_str))

    user_meal_associations = db.session.query(user_meal).filter_by(user_id=current_user.id, date=date).all()
    meals_data = []
    for association in user_meal_associations:
        meal = Meal.query.get(association.meal_id)
        if meal:
            portion_size = association.portion
            meal_data = {
                'meal': meal,
                'name': meal.name,
                'date': association.date,
                'portion': portion_size,
                'calories': meal.calories * (portion_size / 100),
                'proteins': meal.proteins * (portion_size / 100),
                'fats': meal.fats * (portion_size / 100),
                'carbohydrates': meal.carbohydrates * (portion_size / 100),
                'price': meal.price * (portion_size / 100)
            }
            meals_data.append(meal_data)

    total_calories = round(sum(meal['calories'] for meal in meals_data), 2)
    total_proteins = round(sum(meal['proteins'] for meal in meals_data), 2)
    total_fats = round(sum(meal['fats'] for meal in meals_data), 2)
    total_carbohydrates = round(sum(meal['carbohydrates'] for meal in meals_data), 2)
    total_price = round(sum(meal['price'] for meal in meals_data), 2)

    prev_date = date - timedelta(days=1)
    next_date = date + timedelta(days=1)
    today = datetime.today().date()

    return render_template('menu/history.html',
                           today=today,
                           prev_date=prev_date,
                           next_date=next_date,
                           date=date,

                           meals=meals_data,

                           total_calories=total_calories,
                           total_proteins=total_proteins,
                           total_fats=total_fats,
                           total_carbohydrates=total_carbohydrates,
                           total_price=total_price)

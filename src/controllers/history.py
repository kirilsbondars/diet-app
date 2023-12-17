from flask import render_template, session, Flask, redirect, url_for, Blueprint, request
from flask_login import current_user
from src.models.models import db, User, Meal, meals
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/history/')
def history():
    date_str = request.args.get('date_str')
    if date_str is None:
        date = datetime.today().date()
    else:
        try:
            date = datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError:
            today_str = datetime.today().date().strftime('%d.%m.%Y')
            return redirect(url_for('menu.history', date_str=today_str))

    current_user_id = current_user.get_id()

    user_meal_associations = db.session.query(meals).filter_by(user_id=current_user_id, date=date).all()

    meals_data = []
    for association in user_meal_associations:
        meal = Meal.query.get(association.meal_id)
        if meal:
            meals_data.append(meal)

    total_calories = sum(meal.calories for meal in meals_data)
    total_proteins = sum(meal.proteins for meal in meals_data)
    total_fats = sum(meal.fats for meal in meals_data)
    total_carbohydrates = sum(meal.carbohydrates for meal in meals_data)
    total_price = sum(meal.price for meal in meals_data)

    prev_date = date - timedelta(days=1)
    next_date = date + timedelta(days=1)
    today = datetime.today().date()

    return render_template('menu/history.html',
                           today=today.strftime('%d.%m.%Y'),
                           today2=today.strftime('%m-%d-%Y'),
                           meals=meals_data,
                           total_calories=total_calories,
                           total_proteins=total_proteins,
                           total_fats=total_fats,
                           total_carbohydrates=total_carbohydrates,
                           total_price=total_price,
                           prev_date=prev_date.strftime('%d.%m.%Y'),
                           next_date=next_date.strftime('%d.%m.%Y'),
                           date=date.strftime('%d.%m.%Y'))

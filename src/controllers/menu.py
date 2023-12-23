from flask import render_template, request, redirect, url_for, flash
from pulp import LpProblem, LpMinimize, LpVariable, lpSum
from src.models.models import Meal, user_meal, db
from datetime import datetime
from sqlalchemy import insert
from flask_login import current_user


def create_menu_view():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        user = current_user

        user_preferences = get_user_preferences(user)

        # gets meals
        meals = Meal.query.filter_by(**user_preferences).all()

        # error message if no meals found
        if not meals:
            flash('No meals found that match your preferences.', 'error')
            return render_template('menu/create-menu.html', date=date)

        # creates menus
        if meals:
            meals_portions = create_menu(meals, user.calories, user.fats, user.proteins,
                                         user.carbohydrates)
            delete_menu(user.id, date)
            save_menu(meals_portions, user.id, date, 'Breakfast')
            db.session.commit()

            return redirect(url_for('menu.history', date=date))

    return render_template('menu/create-menu.html', today=datetime.today().date())


def create_menu_for_one_day(user, date):
    pass
    # nutrients per mealtime
    # calories = {'Breakfast': 800, 'Lunch': 800, 'Dinner': 800}
    # fats = {'Breakfast': 20, 'Lunch': 30, 'Dinner': 20}
    # proteins = {'Breakfast': 20, 'Lunch': 30, 'Dinner': 20}
    # carbohydrates = {'Breakfast': 100, 'Lunch': 150, 'Dinner': 100}


def get_user_preferences(user):
    user_preferences = {attr: getattr(user, attr) for attr in
                        ['gluten_free', 'vegan', 'vegetarian', 'dairy_free']}
    for preference, value in list(user_preferences.items()):
        if not value:
            del user_preferences[preference]
    return user_preferences


def delete_menu(user_id, date):
    stmt = user_meal.delete().where(user_meal.c.user_id == user_id, user_meal.c.date == date)
    db.session.execute(stmt)


def save_menu(meals_portions, user_id, date, mealtime):
    for meal_id, portion in meals_portions.items():
        stmt = insert(user_meal).values(user_id=user_id, meal_id=meal_id, date=date,
                                        mealtime=mealtime, portion=portion)
        db.session.execute(stmt)


def create_menu(meals, calories, fats, proteins, carbohydrates):
    # Define the problem
    prob = LpProblem("OptimalMenu", LpMinimize)

    # Define the decision variables
    meal_vars = LpVariable.dicts("Meals", [meal.id for meal in meals], 0)

    # Define the objective function
    prob += lpSum([meal_vars[meal.id] * meal.price for meal in meals])

    # Define the constraints
    prob += calories * 1.1 >= lpSum([meal_vars[meal.id] * getattr(meal, 'calories') for meal in meals]) >= calories * 0.9
    prob += fats * 1.1 >= lpSum([meal_vars[meal.id] * getattr(meal, 'fats') for meal in meals]) >= fats * 0.9
    prob += proteins * 1.1 >= lpSum([meal_vars[meal.id] * getattr(meal, 'proteins') for meal in meals]) >= proteins * 0.9
    prob += carbohydrates * 1.1 >= lpSum([meal_vars[meal.id] * getattr(meal, 'carbohydrates') for meal in meals]) >= carbohydrates * 0.9

    # Solve the problem
    prob.solve()

    # Extract and return the solution
    meals_portions = {}
    for v in prob.variables():
        if v.varValue > 0:
            meal_id = int(v.name.split('_')[1])  # Extract the meal ID from the variable name
            meals_portions[meal_id] = round(v.varValue * 100, 2)

    return meals_portions

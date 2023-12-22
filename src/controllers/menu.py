from flask import render_template
from pulp import LpProblem, LpMinimize, LpVariable, lpSum
from src.models.models import Meal, user_meal, db
from datetime import datetime
from sqlalchemy import insert
from flask_login import current_user


def view_menu():
    return render_template('menu/create-menu.html')


def create_one_day_menu(date=datetime.today().date()):
    # delete current menu for this day
    delete_menu(current_user.id, date)

    # nutrients per mealtime
    calories = {'Breakfast': 800, 'Lunch': 800, 'Dinner': 800}
    fats = {'Breakfast': 20, 'Lunch': 30, 'Dinner': 20}
    proteins = {'Breakfast': 20, 'Lunch': 30, 'Dinner': 20}
    carbohydrates = {'Breakfast': 100, 'Lunch': 150, 'Dinner': 100}

    # get user preferences
    user_preferences = {attr: getattr(current_user, attr) for attr in
                        ['gluten_free', 'vegan', 'vegetarian', 'dairy_free']}
    # if a preference is False, remove it from the preferences
    for preference, value in list(user_preferences.items()):
        if not value:
            del user_preferences[preference]

    # create menu for breakfast
    meals = Meal.query.filter_by(
        **user_preferences  # filter meals based on user preferences
    ).all()
    if meals:
        meals_portions = create_menu(meals,
                                     float(current_user.calories),
                                     float(current_user.fats),
                                     float(current_user.proteins),
                                     float(current_user.carbohydrates))
        save_menu(meals_portions, current_user.id, date, 'Breakfast')
        db.session.commit()


def delete_menu(user_id, date):
    stmt = user_meal.delete().where(user_meal.c.user_id == user_id, user_meal.c.date == date)
    db.session.execute(stmt)


def save_menu(meals_portions, user_id, date, mealtime):
    for meal_id, portion in meals_portions.items():
        stmt = insert(user_meal).values(user_id=user_id, meal_id=meal_id, date=date,
                                        mealtime=mealtime, portion=portion)
        db.session.execute(stmt)


def create_menu(meals, calories, fats, proteins, carbohydrates):
    # Use the provided nutritional requirements
    user_requirements = {
        'calories': calories,
        'fats': fats,
        'proteins': proteins,
        'carbohydrates': carbohydrates
    }

    # Define the problem
    prob = LpProblem("OptimalMenu", LpMinimize)

    # Define the decision variables
    meal_vars = LpVariable.dicts("Meals", [meal.id for meal in meals], 0, 3)

    # Define the objective function
    prob += lpSum([meal_vars[meal.id] * float(meal.price) for meal in meals])

    # Define the constraints
    for nutrient in ['calories', 'fats', 'proteins', 'carbohydrates']:
        prob += lpSum([meal_vars[meal.id] * float(getattr(meal, nutrient)) for meal in meals]) >= user_requirements[
            nutrient]

    # Solve the problem
    prob.solve()

    # Extract and return the solution
    meals_portions = {}
    for v in prob.variables():
        if v.varValue > 0:
            meal_id = int(v.name.split('_')[1])  # Extract the meal ID from the variable name
            meals_portions[meal_id] = round(v.varValue * 100, 2)

    return meals_portions

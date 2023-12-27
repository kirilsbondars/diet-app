from flask import render_template, request, redirect, url_for, flash
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value
from src.models.models import Meal, user_meal, db
from datetime import datetime, timedelta, date as d
from sqlalchemy import insert
from flask_login import current_user


def create_menu_view():
    user = current_user
    errors = {}

    if request.method == 'POST':
        # gets inputs
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        n_days_ago = int(request.form['n_days_ago'])
        min_calories = float(request.form['min_calories'])
        max_calories = float(request.form['max_calories'])
        min_fats = float(request.form['min_fats'])
        max_fats = float(request.form['max_fats'])
        min_proteins = float(request.form['min_proteins'])
        max_proteins = float(request.form['max_proteins'])
        min_carbohydrates = float(request.form['min_carbohydrates'])
        max_carbohydrates = float(request.form['max_carbohydrates'])

        # validates inputs
        errors = validate_nutrients()
        if errors:
            return render_template('menu/create-menu.html', form_data=request.form, errors=errors)

        # gets meal ids from last n days
        exclude_meal_ids = get_last_n_days_meal_ids(user.id, date, n_days_ago)

        # gets user preferences
        user_preferences = get_user_preferences(user)

        # gets meals
        meals = Meal.query.filter_by(**user_preferences).filter(~Meal.id.in_(exclude_meal_ids)).all()

        # error message if no meals found
        if not meals:
            flash('No meals found that match your preferences.', 'error')
            return render_template('menu/create-menu.html', form_data=request.form, errors=errors)

        # creates menu
        if meals:
            meals_portions = create_menu(meals, min_calories, max_calories, min_fats, max_fats, min_proteins,
                                         max_proteins, min_carbohydrates, max_carbohydrates)
            delete_menu(user.id, date)
            save_menu(meals_portions, user.id, date)
            db.session.commit()

            return redirect(url_for('menu.history', date=date))

    return render_template('menu/create-menu.html', form_data=request.form, errors=errors, today=d.today())


def validate_nutrients():
    errors = {}

    nutrients = ['calories', 'proteins', 'fats', 'carbohydrates']
    for nutrient in nutrients:
        min_nutrient = request.form.get(f'min_{nutrient}')
        max_nutrient = request.form.get(f'max_{nutrient}')
        if not min_nutrient or not max_nutrient or float(min_nutrient) >= float(max_nutrient):
            errors[nutrient] = ('Invalid input: Min ' + nutrient + ' should be less than Max ' + nutrient +
                                '.')

    return errors


def get_last_n_days_meal_ids(user_id, date, n_days_ago):
    if n_days_ago == 0:
        return []

    date_n_days_ago = date - timedelta(days=n_days_ago)
    meals = db.session.query(user_meal).filter(
        user_meal.c.user_id == user_id,
        user_meal.c.date >= date_n_days_ago,
        user_meal.c.date < date).all()
    if meals:
        return [meal.meal_id for meal in meals]
    else:
        return []


def get_user_preferences(user):
    user_preferences = {attr: getattr(user, attr) for attr in
                        ['gluten_free', 'vegan', 'vegetarian', 'dairy_free']}
    for preference, v in list(user_preferences.items()):
        if not v:
            del user_preferences[preference]
    return user_preferences


def delete_menu(user_id, date):
    stmt = user_meal.delete().where(user_meal.c.user_id == user_id, user_meal.c.date == date)
    db.session.execute(stmt)


def save_menu(meals_portions, user_id, date):
    for meal_id, portion in meals_portions.items():
        stmt = insert(user_meal).values(user_id=user_id, meal_id=meal_id, date=date, portion=portion)
        db.session.execute(stmt)


def create_menu(meals, min_calories, max_calories, min_fats, max_fats, min_proteins, max_proteins, min_carbohydrates,
                max_carbohydrates):
    # Define the problem
    prob = LpProblem("OptimalMenu", LpMinimize)

    # Define the decision variables
    meal_vars = LpVariable.dicts("Meals", [meal.id for meal in meals], 0)

    # Define the objective function
    prob += lpSum([meal_vars[meal.id] * meal.price for meal in meals])

    # Define the constraints
    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'calories') for meal in meals]) >= min_calories
    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'calories') for meal in meals]) <= max_calories

    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'fats') for meal in meals]) >= min_fats
    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'fats') for meal in meals]) <= max_fats

    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'proteins') for meal in meals]) >= min_proteins
    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'proteins') for meal in meals]) <= max_proteins

    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'carbohydrates') for meal in meals]) >= min_carbohydrates
    prob += lpSum([meal_vars[meal.id] * getattr(meal, 'carbohydrates') for meal in meals]) <= max_carbohydrates

    max_meal_size = 5
    prob += lpSum([meal_vars[meal.id] for meal in meals]) <= max_meal_size

    # Solve the problem
    prob.solve()

    # print("The total cost of this balanced diet is: ${}".format(round(value(prob.objective), 2)))
    # print("The total calories of this balanced diet is: {}".format(
    #     round(value(lpSum([meal_vars[meal.id] * getattr(meal, 'calories') for meal in meals])), 2)))
    # print("The total fats of this balanced diet is: {}".format(
    #     round(value(lpSum([meal_vars[meal.id] * getattr(meal, 'fats') for meal in meals])), 2)))
    # print("The total proteins of this balanced diet is: {}".format(
    #     round(value(lpSum([meal_vars[meal.id] * getattr(meal, 'proteins') for meal in meals])), 2)))
    # print("The total carbohydrates of this balanced diet is: {}".format(
    #     round(value(lpSum([meal_vars[meal.id] * getattr(meal, 'carbohydrates') for meal in meals])), 2)))

    # Extract and return the solution
    meals_portions = {}
    for v in prob.variables():
        if v.varValue > 0:
            meal_id = int(v.name.split('_')[1])  # Extract the meal ID from the variable name
            meals_portions[meal_id] = v.varValue

    return meals_portions

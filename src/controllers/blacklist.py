from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user

from models.models import blacklisted_meals, Meal
from models.models import db


def view():
    meals = (db.session.query(Meal)
             .join(blacklisted_meals, Meal.id == blacklisted_meals.c.meal_id)
             .filter(blacklisted_meals.c.user_id == current_user.id)
             .all())
    return render_template('menu/blacklist.html', meals=meals)


def add(meal_id, history_date):
    meal = db.session.query(Meal).get(meal_id)
    if meal:
        new_blacklist = blacklisted_meals.insert().values(meal_id=meal_id, user_id=current_user.id)
        try:
            db.session.execute(new_blacklist)
            db.session.commit()
            flash(f'Meal "{meal.name}" has been added to blacklist! '
                  f'Please regenerate menu for it to exclude "{meal.name}"', 'success')
        except:
            db.session.rollback()
            flash(f'Error! Could not add meal "{meal.name}" to blacklist!', 'danger')

    return redirect(url_for('menu.history', date=history_date))


def remove(meal_id, return_page, history_date):
    stmt = blacklisted_meals.delete().where(
        blacklisted_meals.c.meal_id == meal_id,
        blacklisted_meals.c.user_id == current_user.id
    )
    result = db.session.execute(stmt)
    db.session.commit()

    meal = db.session.query(Meal).get(meal_id)

    if result:
        flash(f'Meal "{meal.name}" has been removed from blacklist! '
              f'Please regenerate menu for it to include "{meal.name}"', 'success')
    else:
        flash(f'Meal "{meal.name}" is not in blacklist!', 'danger')

    if return_page == 'history':
        return redirect(url_for('menu.history', date=history_date))
    elif return_page == 'blacklist':
        return redirect(url_for('blacklist.view'))

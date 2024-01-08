import os
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from models.models import User, db, Meal


@login_required
def admin_panel():
    if not current_user.is_admin:
        flash('Access denied: You must be an admin to view this page.')
        return redirect(url_for('index.render_page_index'))
    users = User.query.all()
    meals = Meal.query.all()
    return render_template('menu/admin-panel.html', users=users, meals=meals)


def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully.')
    return redirect(url_for('admin.admin_panel'))


def user_details(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template('menu/user_details.html', user=user)
    return redirect(url_for('admin.admin_panel'))


def add_meal():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        calories = request.form['calories']
        proteins = request.form['proteins']
        fats = request.form['fats']
        carbohydrates = request.form['carbohydrates']
        gluten_free = request.form.get('gluten_free') == 'on'
        vegan = request.form.get('vegan') == 'on'
        vegetarian = request.form.get('vegetarian') == 'on'
        dairy_free = request.form.get('dairy_free') == 'on'

        image = request.files['image']
        filename = secure_filename(image.filename) if image else None
        if filename:
            image_path = os.path.join('static/images', filename)
            image.save(image_path)

        new_meal = Meal(
            name=name,
            image_src=filename,
            price=price,
            calories=calories,
            proteins=proteins,
            fats=fats,
            carbohydrates=carbohydrates,
            gluten_free=gluten_free,
            vegan=vegan,
            vegetarian=vegetarian,
            dairy_free=dairy_free,
        )

        db.session.add(new_meal)
        db.session.commit()
        flash('Meal added successfully!')
        return redirect(url_for('admin.admin_panel'))

    return render_template('menu/add_meal.html')

def edit_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    if request.method == 'POST':
        meal.name = request.form['name']
        meal.price = request.form['price']
        meal.calories = request.form['calories']
        meal.proteins = request.form['proteins']
        meal.fats = request.form['fats']
        meal.carbohydrates = request.form['carbohydrates']
        meal.gluten_free = 'gluten_free' in request.form
        meal.vegan = 'vegan' in request.form
        meal.vegetarian = 'vegetarian' in request.form
        meal.dairy_free = 'dairy_free' in request.form
        meal.for_breakfast = 'for_breakfast' in request.form
        meal.for_lunch = 'for_lunch' in request.form
        meal.for_dinner = 'for_dinner' in request.form

        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('static/images', filename)
            image.save(image_path)
            meal.image_src = filename

        db.session.commit()
        flash('Meal updated successfully!')
        return redirect(url_for('admin.admin_panel'))

    return render_template('menu/edit_meal.html', meal=meal)


def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    db.session.delete(meal)
    db.session.commit()
    flash('Meal deleted successfully.')
    return redirect(url_for('admin.admin_panel'))

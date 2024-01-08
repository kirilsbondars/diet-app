from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime

from models.models import db, User

bcrypt = Bcrypt()


def profile():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        gender = request.form.get("gender")
        date_of_birth = datetime.strptime(request.form.get("date_of_birth"), "%Y-%m-%d").date()
        weight = request.form.get("weight")
        height = request.form.get("height")
        gluten_free = request.form.get("gluten-free") == 'on'
        vegan = request.form.get("vegan") == 'on'
        vegetarian = request.form.get("vegetarian") == 'on'
        dairy_free = request.form.get("dairy-free") == 'on'

        current_user.name = name
        current_user.surname = surname
        current_user.gender = gender
        current_user.date_of_birth = date_of_birth
        current_user.weight = weight
        current_user.height = height
        current_user.gluten_free = gluten_free
        current_user.vegan = vegan
        current_user.vegetarian = vegetarian
        current_user.dairy_free = dairy_free

        (min_calories, max_calories, min_fats, max_fats, min_proteins, max_proteins, min_carbohydrates,
         max_carbohydrates) = calculate_min_max_nutrients(weight, height, date_of_birth, gender)
        current_user.min_calories = min_calories
        current_user.max_calories = max_calories
        current_user.min_fats = min_fats
        current_user.max_fats = max_fats
        current_user.min_proteins = min_proteins
        current_user.max_proteins = max_proteins
        current_user.min_carbohydrates = min_carbohydrates
        current_user.max_carbohydrates = max_carbohydrates

        if 'min_calories' in request.form:
            # Capture nutrient information from the form
            min_calories = float(request.form.get("min_calories"))
            max_calories = float(request.form.get("max_calories"))
            min_fats = float(request.form.get("min_fats"))
            max_fats = float(request.form.get("max_fats"))
            min_proteins = float(request.form.get("min_proteins"))
            max_proteins = float(request.form.get("max_proteins"))
            min_carbohydrates = float(request.form.get("min_carbohydrates"))
            max_carbohydrates = float(request.form.get("max_carbohydrates"))

            # Update the current user's nutrient data
            current_user.min_calories = min_calories
            current_user.max_calories = max_calories
            current_user.min_fats = min_fats
            current_user.max_fats = max_fats
            current_user.min_proteins = min_proteins
            current_user.max_proteins = max_proteins
            current_user.min_carbohydrates = min_carbohydrates
            current_user.max_carbohydrates = max_carbohydrates

        db.session.commit()

        flash('Your data has been saved.', 'success')

        return redirect(url_for("auth.profile"))

    return render_template("auth/profile.html")


def sing_up():
    errors = {}
    form_data = {}
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")
        gender = request.form.get("gender")
        date_of_birth = datetime.strptime(request.form.get("date_of_birth"), "%Y-%m-%d").date()
        weight = request.form.get("weight")
        height = request.form.get("height")
        gluten_free = request.form.get("gluten-free") == 'on'
        vegan = request.form.get("vegan") == 'on'
        vegetarian = request.form.get("vegetarian") == 'on'
        dairy_free = request.form.get("dairy-free") == 'on'

        form_data = {
            "name": name,
            "surname": surname,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "weight": weight,
            "height": height,
            "gluten_free": gluten_free,
            "vegan": vegan,
            "vegetarian": vegetarian,
            "dairy_free": dairy_free
        }

        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            errors['email'] = 'Email already used by someone else'

        if errors:
            return render_template('auth/sign_up.html', errors=errors, form_data=form_data)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        (min_calories, max_calories, min_fats, max_fats, min_proteins, max_proteins, min_carbohydrates,
         max_carbohydrates) = calculate_min_max_nutrients(weight, height, date_of_birth, gender)
        user = User(name=name, surname=surname, email=email, password=hashed_password, gender=gender,
                    date_of_birth=date_of_birth, weight=weight, height=height, gluten_free=gluten_free, vegan=vegan,
                    vegetarian=vegetarian, dairy_free=dairy_free, min_calories=min_calories, max_calories=max_calories,
                    min_fats=min_fats, max_fats=max_fats, min_proteins=min_proteins, max_proteins=max_proteins,
                    min_carbohydrates=min_carbohydrates, max_carbohydrates=max_carbohydrates)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for("auth.login"))
    return render_template("auth/sign_up.html", errors=errors, form_data=form_data)


def login():
    form_data = {}
    error = ''

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        form_data = {
            "email": email,
            "password": password
        }

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("menu.create_menu_view"))
        else:
            error = 'Invalid username or password'
    return render_template("auth/login.html", form_data=form_data, error=error)


def logout():
    logout_user()
    return redirect(url_for("auth.login"))


def calculate_min_max_nutrients(weight, height, date_of_birth, gender):
    # Calculate base nutrients
    weight = float(weight)
    height = float(height)

    # Calculate age
    today = datetime.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    if gender == "Male":
        calories = (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)) * 1.375
    else:
        calories = (447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)) * 1.375

    fat_percentage = 30
    protein_percentage = 20
    carb_percentage = 50

    fats = (fat_percentage / 100) * calories / 9
    proteins = (protein_percentage / 100) * calories / 4
    carbohydrates = (carb_percentage / 100) * calories / 4

    # Calculate min and max nutrients
    min_calories, max_calories = calories * 0.9, calories * 1.1
    min_fats, max_fats = fats * 0.9, fats * 1.1
    min_proteins, max_proteins = proteins * 0.9, proteins * 1.1
    min_carbohydrates, max_carbohydrates = carbohydrates * 0.9, carbohydrates * 1.1

    # Round the values
    min_calories, max_calories = round(min_calories), round(max_calories)
    min_fats, max_fats = round(min_fats), round(max_fats)
    min_proteins, max_proteins = round(min_proteins), round(max_proteins)
    min_carbohydrates, max_carbohydrates = round(min_carbohydrates), round(max_carbohydrates)

    return (min_calories, max_calories, min_fats, max_fats, min_proteins, max_proteins, min_carbohydrates,
            max_carbohydrates)

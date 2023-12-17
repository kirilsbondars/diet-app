from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from flask_bcrypt import Bcrypt

from src.models.models import db, User

bcrypt = Bcrypt()


def profile():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        gender = request.form.get("gender")
        age = request.form.get("age")
        weight = request.form.get("weight")
        height = request.form.get("height")
        gluten_free = request.form.get("gluten-free") == 'on'
        vegan = request.form.get("vegan") == 'on'
        vegetarian = request.form.get("vegetarian") == 'on'
        dairy_free = request.form.get("dairy-free") == 'on'

        calories, fats, proteins, carbohydrates = calculate_calories(weight, height, age, gender)

        current_user.name = name
        current_user.surname = surname
        current_user.gender = gender
        current_user.age = age
        current_user.weight = weight
        current_user.height = height
        current_user.gluten_free = gluten_free
        current_user.vegan = vegan
        current_user.vegetarian = vegetarian
        current_user.dairy_free = dairy_free
        current_user.calories = calories
        current_user.fats = fats
        current_user.proteins = proteins
        current_user.carbohydrates = carbohydrates

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
        age = request.form.get("age")
        weight = request.form.get("weight")
        height = request.form.get("height")
        gluten_free = request.form.get("gluten-free") == 'on'
        vegan = request.form.get("vegan") == 'on'
        vegetarian = request.form.get("vegetarian") == 'on'
        dairy_free = request.form.get("dairy-free") == 'on'

        calories, fats, proteins, carbohydrates = calculate_calories(weight, height, age, gender)

        form_data = {
            "name": name,
            "surname": surname,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
            "gender": gender,
            "age": age,
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
        user = User(name=name, surname=surname, email=email, password=hashed_password, gender=gender,
                    age=age, weight=weight, height=height, gluten_free=gluten_free, vegan=vegan,
                    vegetarian=vegetarian, dairy_free=dairy_free, calories=calories, fats=fats, proteins=proteins, carbohydrates=carbohydrates)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))
    return render_template("auth/sign_up.html", errors=errors, form_data=form_data)


def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user and bcrypt.check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("index.render_page_index"))
    return render_template("auth/login.html")


def logout():
    logout_user()
    return redirect(url_for("index.render_page_index"))


def calculate_calories(weight, height, age, gender):
    if gender == "male":
        calories = (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)) * 1.375
    else:
        calories = (447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)) * 1.375

    fat_percentage = 30
    protein_percentage = 20
    carb_percentage = 50

    fats = (fat_percentage / 100) * calories / 9
    proteins = (protein_percentage / 100) * calories / 4
    carbohydrates = (carb_percentage / 100) * calories / 4

    return calories, fats, proteins, carbohydrates

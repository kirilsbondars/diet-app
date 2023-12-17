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
                    vegetarian=vegetarian, dairy_free=dairy_free)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))
    return render_template("auth/sign_up.html", errors=errors, form_data=form_data)


def login():
    error = ''

    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user and bcrypt.check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("index.render_page_index"))
        else:
            error = 'Invalid username or password'
    return render_template("auth/login.html", error=error)


def logout():
    logout_user()
    return redirect(url_for("index.render_page_index"))

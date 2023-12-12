from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_bcrypt import Bcrypt

from src.models.models import db, User

bcrypt = Bcrypt()



def profile():
    # Pass the existing user data to the template
    form_data = {
        "name": current_user.name,
        "surname": current_user.surname,
        "gender": current_user.gender,
        "age": current_user.age,
        "weight": current_user.weight,
        "height": current_user.height,
        "gluten_free": current_user.gluten_free,
        "vegan": current_user.vegan,
        "vegetarian": current_user.vegetarian,
        "dairy_free": current_user.dairy_free
    }

    if request.method == "POST":
        print("Form submitted")
        # Retrieve form data
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

        # Update the user object with the new data
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

        # Commit the changes to the database
        db.session.commit()

        return redirect(url_for("auth.profile"))

    return render_template("auth/profile.html",form_data=form_data)


def sing_up():
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

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, surname=surname, email=email, password=hashed_password, gender=gender,
                    age=age, weight=weight, height=height, gluten_free=gluten_free, vegan=vegan,
                    vegetarian=vegetarian, dairy_free=dairy_free)
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

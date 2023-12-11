from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_bcrypt import Bcrypt
from src.models.models import db, User

bcrypt = Bcrypt()


def profile():
    return render_template("auth/profile.html")


def sing_up():
    if request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8')
        user = User(username=request.form.get("username"),
                    password=hashed_password,
                    email='jj@jjj.jj',
                    name='aa',
                    surname='aa',
                    age=1,
                    weight=1,
                    height=1,
                    gender='Male',
                    calories=100,
                    proteins=100,
                    fats=20,
                    carbohydrates=30,
                    gluten_free=True,
                    vegan=True,
                    vegeratian=False,
                    dairy_free=True)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("auth/sign_up.html")


def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form.get("username")).first()
        if user and bcrypt.check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("index.render_page_index"))
        else:
            return render_template("auth/login_error.html")
    return render_template("auth/login.html")


def logout():
    logout_user()
    return redirect(url_for("index.render_page_index"))

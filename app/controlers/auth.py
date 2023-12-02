from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_bcrypt import Bcrypt
from app.models.models import db, Users

bcrypt = Bcrypt()


def sing_up():
    if request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8')
        user = Users(username=request.form.get("username"),
                     password=hashed_password,
                     email=request.form.get("email"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("auth/sign_up.html")



def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user and bcrypt.check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("menu.view"))
    return render_template("auth/login.html")


def logout():
    logout_user()
    return redirect(url_for("auth/login.html"))

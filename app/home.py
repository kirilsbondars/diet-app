from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Users

home = Blueprint('home', __name__)


@home.route('/')
def view():
    return render_template("others/home.html")

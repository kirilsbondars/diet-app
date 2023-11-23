from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Tasks, Person, Address
from flask_login import login_required

tasks = Blueprint('tasks', __name__)


@tasks.route('/')
@login_required
def view():
    task_list = Tasks.query.all()
    person = Person.query.first()
    return render_template("others/tasks.html", tasks=task_list, person=person)

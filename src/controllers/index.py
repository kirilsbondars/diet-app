from flask import render_template
from src.models.models import db, Tasks, User


def render_page_index():
    tasks = Tasks(
        description='This is a test task'
    )
    db.session.add(tasks)

    user = User.query.first()
    meals = user.meals
    for meal in meals:
        print(meal.name)

    task_list = Tasks.query.all()
    return render_template('index.html', tasks=task_list)

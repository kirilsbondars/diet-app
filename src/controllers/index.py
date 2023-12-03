from flask import render_template
from src.models.models import db, Tasks


def render_page_index():
    tasks = Tasks(
        description='This is a test task'
    )
    db.session.add(tasks)
    db.session.commit()

    task_list = Tasks.query.all()
    return render_template('index.html', tasks=task_list)

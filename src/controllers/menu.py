from flask import render_template
from models.models import db, Tasks

def index():
    tasks = Tasks(
        description='This is a test task'
    )
    db.session.add(tasks)
    db.session.commit()

    task_list = Tasks.query.all()
    return render_template('menu/index.html', tasks=task_list)
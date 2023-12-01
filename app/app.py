from flask import Flask
from flask_login import LoginManager

from models.models import db, Users, Tasks
from models.import_data import import_data

from auth import auth
from tasks import tasks
from menu import menu

from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"

db.init_app(app)
with app.app_context():
    db.create_all()
    import_data(db, Tasks)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def loader_user(user_id):
    return db.session.get(Users, user_id)


app.register_blueprint(auth)
app.register_blueprint(tasks, url_prefix='/tasks')
app.register_blueprint(menu, url_prefix='/menu')

if __name__ == "__main__":
    app.run(debug=True)

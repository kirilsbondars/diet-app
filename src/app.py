from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5

from routes.index import index_blueprint
from routes.auth import auth_blueprint
from routes.menu import menu_blueprint
from routes.blacklist import blacklist_blueprint
from src.models.models import db, User
from src.models.import_data import import_data


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def loader_user(user_id):
        return db.session.get(User, user_id)

    Bootstrap5(app)

    # fill db
    with app.app_context():
        import_data()

    return app


app = create_app()

app.register_blueprint(index_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(menu_blueprint)
app.register_blueprint(blacklist_blueprint)


if __name__ == '__main__':
    app.run()

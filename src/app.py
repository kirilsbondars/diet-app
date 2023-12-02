from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5

from routes.index import index_blueprint
from models.models import db, Users, Tasks


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
        return db.session.get(Users, user_id)

    bootstrap = Bootstrap5(app)

    return app


app = create_app()

app.register_blueprint(index_blueprint)


if __name__ == '__main__':
    app.run()

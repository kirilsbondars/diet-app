from flask import Flask
from routes.menu import blueprint
from models.models import db


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database
    with app.app_context():
        db.create_all()
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/menu')


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

meals = db.Table('user_meal',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                 db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True),
                 db.Column('date', db.Date, primary_key=True),
                 db.Column('mealtime', db.Enum('Breakfast', 'Lunch', 'Dinner'), primary_key=True),
                 )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)

    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)

    calories = db.Column(db.Integer, nullable=True)
    proteins = db.Column(db.Integer, nullable=True)
    fats = db.Column(db.Integer, nullable=True)
    carbohydrates = db.Column(db.Integer, nullable=True)

    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegeratian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)

    meals = db.relationship('Meal', secondary=meals, lazy='subquery',
                            backref=db.backref('pages', lazy=True))


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    image_src = db.Column(db.String(250), nullable=True)
    price = db.Column(db.Float, nullable=False)

    calories = db.Column(db.Integer, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)

    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegeratian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)

    for_breakfast = db.Column(db.Boolean, nullable=False)
    for_lunch = db.Column(db.Boolean, nullable=False)
    for_dinner = db.Column(db.Boolean, nullable=False)

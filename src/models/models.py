from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

meals = db.Table('user_meal',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                 db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True),
                 db.Column('date', db.Date, primary_key=True),
                 db.Column('mealtime', db.Enum('Breakfast', 'Lunch', 'Dinner'), primary_key=True),
                 db.Column('portion', db.Float(2), nullable=False),
                 )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)

    date_of_birth = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float(2), nullable=False)
    height = db.Column(db.Float(2), nullable=False)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)

    calories = db.Column(db.Float(2), nullable=True)
    proteins = db.Column(db.Float(2), nullable=True)
    fats = db.Column(db.Float(2), nullable=True)
    carbohydrates = db.Column(db.Float(2), nullable=True)

    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)

    meals = db.relationship('Meal', secondary=meals, lazy='subquery',
                            backref=db.backref('pages', lazy=True))


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    image_src = db.Column(db.String(250), nullable=True)
    price = db.Column(db.Float(2), nullable=False)

    calories = db.Column(db.Float(2), nullable=False)
    proteins = db.Column(db.Float(2), nullable=False)
    fats = db.Column(db.Float(2), nullable=False)
    carbohydrates = db.Column(db.Float(2), nullable=False)

    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)

    for_breakfast = db.Column(db.Boolean, nullable=False)
    for_lunch = db.Column(db.Boolean, nullable=False)
    for_dinner = db.Column(db.Boolean, nullable=False)

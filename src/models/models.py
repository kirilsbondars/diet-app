from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Float

db = SQLAlchemy()

user_meal = db.Table('user_meal',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                     db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True),
                     db.Column('date', db.Date, primary_key=True),
                     db.Column('portion', Float(12, False, 2), nullable=False),
                     )

meal_blacklist = db.Table('meal_blacklist',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                          db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True)
                          )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)

    date_of_birth = db.Column(db.Date, nullable=False)
    weight = db.Column(Float(12, False, 2), nullable=False)
    height = db.Column(Float(12, False, 2), nullable=False)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)

    min_calories = db.Column(Float(12, False, 2), nullable=True)
    max_calories = db.Column(Float(12, False, 2), nullable=True)
    min_proteins = db.Column(Float(12, False, 2), nullable=True)
    max_proteins = db.Column(Float(12, False, 2), nullable=True)
    min_fats = db.Column(Float(12, False, 2), nullable=True)
    max_fats = db.Column(Float(12, False, 2), nullable=True)
    min_carbohydrates = db.Column(Float(12, False, 2), nullable=True)
    max_carbohydrates = db.Column(Float(12, False, 2), nullable=True)

    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)

    meals = db.relationship('Meal', secondary=user_meal, lazy='subquery',
                            backref=db.backref('users', lazy=True))
    meals_blacklist = db.relationship('Meal', secondary=meal_blacklist, lazy='subquery',
                                      backref=db.backref('in_users_blacklist', lazy=True))


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    image_src = db.Column(db.String(250), nullable=True)
    price = db.Column(Float(12, False, 2), nullable=False)

    calories = db.Column(Float(12, False, 2), nullable=False)
    proteins = db.Column(Float(12, False, 2), nullable=False)
    fats = db.Column(Float(12, False, 2), nullable=False)
    carbohydrates = db.Column(Float(12, False, 2), nullable=False)

    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)

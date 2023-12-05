from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

meals = db.Table('meals',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                 db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True),
                 db.Column('date', db.Date, primary_key=True),
                 db.Column('mealtime_id', db.Integer, db.ForeignKey('mealtime.id'), primary_key=True),
                 )


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    users = db.relationship('User', backref='gender', lazy=True)


class UserNutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calories = db.Column(db.Integer, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)
    users = db.relationship('User', backref='nutrition', lazy=True)


class UserFoodPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegeratian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)
    users = db.relationship('User', backref='food_preference', lazy=True)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    nutrition_id = db.Column(db.Integer, db.ForeignKey('user_nutrition.id'), nullable=True)
    food_preference_id = db.Column(db.Integer, db.ForeignKey('user_food_preference.id'), nullable=True)
    meals = db.relationship('Meal', secondary=meals, lazy='subquery',
                            backref=db.backref('pages', lazy=True))


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    portion = db.Column(db.Integer, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)
    gluten_free = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    vegeratian = db.Column(db.Boolean, nullable=False)
    dairy_free = db.Column(db.Boolean, nullable=False)


class Mealtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)

from src.models.models import db, Meal, User, meals
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()


def import_meals():
    if Meal.query.first() is None:
        meal = Meal(id=1, name='Pasta', calories=100, portion=100,
                    proteins=100, fats=20, carbohydrates=30, gluten_free=True,
                    vegan=True, vegeratian=False, dairy_free=True, mealtime='Breakfast')
        db.session.add(meal)
        db.session.commit()


def import_users():
    if User.query.first() is None:
        hashed_password = bcrypt.generate_password_hash('123').decode('utf-8')
        user = User(username='123',
                    password=hashed_password,
                    email='jj@jjj.jj',
                    name='aa',
                    surname='aa',
                    age=1,
                    weight=1,
                    height=1,
                    gender='Male',
                    calories=100,
                    proteins=100,
                    fats=20,
                    carbohydrates=30,
                    gluten_free=True,
                    vegan=True,
                    vegeratian=False,
                    dairy_free=True)
        db.session.add(user)
        db.session.commit()


def import_meal_user():
    user = User.query.first()
    meal = Meal.query.first()
    if user is not None and meal is not None:
        existing_record = db.session.query(meals).first()
        if existing_record is None:
            db.session.execute(meals.insert().values(user_id=user.id, meal_id=meal.id, date=datetime.now(), mealtime='Breakfast'))
            db.session.commit()


def import_data():
    import_meals()
    import_users()
    import_meal_user()



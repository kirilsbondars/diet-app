from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy import insert, select
import csv
import os

from models.models import db, Meal, User, user_meal

bcrypt = Bcrypt()


def import_meals():
    csv_filename = os.path.join(os.path.dirname(__file__), 'meals.csv')
    if Meal.query.first() is None:
        print("Importing meals...")

        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            meals_reader = csv.DictReader(csvfile, delimiter=';')

            for row in meals_reader:
                meal = Meal(
                    id=int(row['id']),
                    name=row['name'],
                    image_src=row['image_src'],
                    price=float(row['price']),
                    calories=float(row['calories']),
                    proteins=float(row['proteins']),
                    fats=float(row['fats']),
                    carbohydrates=float(row['carbohydrates']),
                    gluten_free=row['gluten_free'].lower() == 'true',
                    vegan=row['vegan'].lower() == 'true',
                    vegetarian=row['vegetarian'].lower() == 'true',
                    dairy_free=row['dairy_free'].lower() == 'true')
                db.session.add(meal)
        db.session.commit()


def import_test_user():
    if User.query.first() is None:
        print("Importing test user...")
        test_user = User(
            email="test@test.test",
            password=bcrypt.generate_password_hash("123").decode('utf-8'),
            name="Test",
            surname="Test",
            date_of_birth=datetime(1990, 1, 1),
            weight=70.0,
            height=170.0,
            gender="Male",
            gluten_free=False,
            vegan=False,
            vegetarian=False,
            dairy_free=False,
            min_calories=1500,
            max_calories=2220,
            min_proteins=50,
            max_proteins=200,
            min_fats=50,
            max_fats=200,
            min_carbohydrates=50,
            max_carbohydrates=200
        )
        db.session.add(test_user)
        db.session.commit()


def import_test_user_meal():
    if db.session.execute(select(user_meal)).first() is None:
        print("Importing test user meal...")
        user = User.query.first()
        meal = Meal.query.first()
        user_meal_record = insert(user_meal).values(user_id=user.id, meal_id=meal.id, date=datetime.now(), portion=200)

        db.session.execute(user_meal_record)
        db.session.commit()


def import_data():
    import_meals()
    import_test_user()




from src.models.models import db, Meal, User, user_meal
from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy import insert, select
import csv

bcrypt = Bcrypt()


def import_meals(csv_filename='models/meals.csv'):  # change file name
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
                    gluten_free=row['gluten_free'].lower() == 'True',
                    vegan=row['vegan'].lower() == 'True',
                    vegetarian=row['vegetarian'].lower() == 'True',
                    dairy_free=row['dairy_free'].lower() == 'True',
                    for_breakfast=row['for_breakfast'].lower() == 'True',
                    for_lunch=row['for_lunch'].lower() == 'True',
                    for_dinner=row['for_dinner'].lower() == 'True',)
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
            calories=2000,
            proteins=100,
            fats=100,
            carbohydrates=100
        )
        db.session.add(test_user)
        db.session.commit()


def import_test_user_meal():
    if db.session.execute(select(user_meal)).first() is None:
        print("Importing test user meal...")
        user = User.query.first()
        meal = Meal.query.first()
        user_meal_record = insert(user_meal).values(user_id=user.id, meal_id=meal.id, date=datetime.now(),
                                                    mealtime='Breakfast', portion=200)

        db.session.execute(user_meal_record)
        db.session.commit()


def import_data():
    import_meals()
    import_test_user()
    # import_test_user_meal()




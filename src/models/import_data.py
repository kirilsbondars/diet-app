import csv

from src.models.models import db, Meal, User, meals
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()

#
# def import_meals():
#     if Meal.query.first() is None:
#         meal = Meal(id=1, name='Pasta', price=100, calories=100, portion=100,
#                     proteins=100, fats=20, carbohydrates=30, gluten_free=True,
#                     vegan=True, vegetarian=False, dairy_free=True,
#                     for_breakfast=True, for_lunch=True, for_dinner=True)
#         db.session.add(meal)
#         db.session.commit()

def import_meals(csv_filename='models/meals.csv'):  # change file name
    if Meal.query.first() is None:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            meals_reader = csv.DictReader(csvfile, delimiter=';')

            for row in meals_reader:
                print(row)
                meal = Meal(
                    id=int(row['id']),
                    name=row['name'],
                    image_src=row['image_src'],
                    price=float(row['price']),
                    calories=float(row['calories']),
                    # portion=int(row['portion']),
                    proteins=float(row['proteins']),
                    fats=float(row['fats']),
                    carbohydrates=float(row['carbohydrates']),
                    gluten_free=row['gluten_free'].lower() == 'True',
                    vegan=row['vegan'].lower() == 'True',
                    vegeratian=row['vegetarian'].lower() == 'True',
                    dairy_free=row['dairy_free'].lower() == 'True',
                    for_breakfast=row['for_breakfast'].lower() == 'True',
                    for_lunch=row['for_lunch'].lower() == 'True',
                    for_dinner=row['for_dinner'].lower() == 'True',)
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




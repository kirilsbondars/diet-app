from src.models.models import db, Meal
from flask_bcrypt import Bcrypt
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
                    gluten_free=row['gluten_free'].lower() == 'true',
                    vegan=row['vegan'].lower() == 'true',
                    vegetarian=row['vegetarian'].lower() == 'true',
                    dairy_free=row['dairy_free'].lower() == 'true',
                    for_breakfast=row['for_breakfast'].lower() == 'true',
                    for_lunch=row['for_lunch'].lower() == 'true',
                    for_dinner=row['for_dinner'].lower() == 'true',)
                db.session.add(meal)
        db.session.commit()


def import_data():
    import_meals()




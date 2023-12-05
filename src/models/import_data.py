from src.models.models import db, Gender, Meal, User, meals, Mealtime, UserNutrition, UserFoodPreference
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()


def import_genders():
    if Gender.query.first() is None:
        gender_male = Gender(id=1, name='Male')
        gender_female = Gender(id=2, name='Female')
        genders = [gender_male, gender_female]

        db.session.add_all(genders)
        db.session.commit()


def import_meals():
    if Meal.query.first() is None:
        meal = Meal(id=1, name='Pasta', calories=100, portion=100,
                    proteins=100, fats=20, carbohydrates=30, gluten_free=True,
                    vegan=True, vegeratian=False, dairy_free=True)
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
                    gender_id=1,
                    nutrition_id=1,
                    food_preference_id=1)
        db.session.add(user)
        db.session.commit()


def import_meal_user():
    user = User.query.first()
    meal = Meal.query.first()
    if user is not None and meal is not None:
        existing_record = db.session.query(meals).first()
        if existing_record is None:
            db.session.execute(meals.insert().values(user_id=user.id, meal_id=meal.id, date=datetime.now(), mealtime_id=1))
            db.session.commit()


def import_mealtime():
    if Mealtime.query.first() is None:
        breakfast = Mealtime(id='1', name='Breakfast')
        lunch = Mealtime(id='2', name='Lunch')
        dinner = Mealtime(id='3', name='Dinner')
        mealtimes = [breakfast, lunch, dinner]

        db.session.add_all(mealtimes)
        db.session.commit()


def import_user_nutrition():
    if UserNutrition.query.first() is None:
        user_nutrition = UserNutrition(id=1, calories=100, proteins=100, fats=20, carbohydrates=30)
        db.session.add(user_nutrition)
        db.session.commit()


def import_user_food_preference():
    if UserFoodPreference.query.first() is None:
        user_food_preference = UserFoodPreference(id=1, gluten_free=True, vegan=True, vegeratian=False, dairy_free=True)
        db.session.add(user_food_preference)
        db.session.commit()


def import_data():
    import_mealtime()
    import_genders()
    import_meals()
    import_user_nutrition()
    import_user_food_preference()
    import_users()
    import_meal_user()



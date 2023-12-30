from wtforms import Form, IntegerField, validators, DateField


class MenuForm(Form):
    date = DateField('Date', [validators.DataRequired()])
    n_days_ago = IntegerField('Exclude meals from last n days', [validators.DataRequired()])
    min_calories = IntegerField('Calories min', [
        validators.DataRequired(),
        validators.NumberRange(min=1),
        validators.EqualTo('max_calories', message='Passwords must match')
    ])
    max_calories = IntegerField('Calories max', [validators.DataRequired()])
    min_proteins = IntegerField('Proteins min', [validators.DataRequired()])
    max_proteins = IntegerField('Proteins max', [validators.DataRequired()])
    min_fats = IntegerField('Fats min', [validators.DataRequired()])
    max_fats = IntegerField('Fats max', [validators.DataRequired()])
    min_carbohydrates = IntegerField('Carbohydrates min', [validators.DataRequired()])
    max_carbohydrates = IntegerField('Carbohydrates max', [validators.DataRequired()])
import requests
import csv
import os

# Define the API endpoint
url = "https://api.spoonacular.com/recipes/complexSearch"  # Spoonacular API endpoint

# Define the parameters for the API request
params = {
    "apiKey": "6ee5549013ac493f8b9307f2dde38be6",  # Replace with your actual API key
    "number": 1,
    "addRecipeNutrition": True,
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Parse the response as JSON
data = response.json()

# Extract the meals
meals = data['results']

# Open the CSV file in append mode
csv_filename = os.path.join(os.path.dirname(__file__), 'meals_test.csv')
with open(csv_filename, 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    # Write the information for each meal
    for meal in meals:
        writer.writerow([
            meal['id'],
            meal['title'],
            '',
            meal['pricePerServing'],
            meal['nutrition']['nutrients'][0]['amount'],  # Calories
            meal['nutrition']['nutrients'][1]['amount'],  # Proteins
            meal['nutrition']['nutrients'][2]['amount'],  # Fats
            meal['nutrition']['nutrients'][3]['amount'],  # Carbohydrates
            meal['glutenFree'],
            meal['vegan'],
            meal['vegetarian'],
            meal['dairyFree']
        ])
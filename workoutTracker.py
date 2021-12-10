# workoutTracker.py
#
# Python Bootcamp Day 38 - Workout Tracker
# Usage:
#      Track your workouts using natural language with the NutritionIX API and
# Sheety.
#
# Marceia Egler December 10, 2021

import os
from dotenv import load_dotenv
import requests
from datetime import datetime as dt
import json

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITION_ID = os.getenv("APP_ID")
NUTRITION_API = os.getenv("API_KEY")
SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")
AGE = 25
GENDER = "female"
HEIGHT = 160.02
WEIGHT = 54.4311
TODAY = dt.now().strftime("%d%m%Y")
TIME = dt.now().strftime("%H:%M")

token = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API,
}

ask_for_exercise = input("Tell me which exercises you did: ")

exercise_data = {
    "query": ask_for_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

nutrition_post_req = requests.post(
    url=NUTRITION_ENDPOINT, json=exercise_data, headers=token
)

resp_text = nutrition_post_req.text
dict = json.loads(resp_text)

# Confirm you are connected to your chosen spreadsheet.

# read_sheety = requests.get(url=SHEETY_ENDPOINT)
# read_sheety.raise_for_status()
# sheety_data = read_sheety.json()
# print(sheety_data)

for i, v in enumerate(dict["exercises"]):

    exercise_type = dict["exercises"][i]["name"]
    exercise_duration = dict["exercises"][i]["duration_min"]
    exercise_calories = dict["exercises"][i]["nf_calories"]

    sheety_header = {
        "Authorization": SHEETY_API_KEY,
        "Content-Type": "application/json",
    }

    sheety_data_to_post = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": exercise_type.title(),
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }
    post_sheety = requests.post(
        url=SHEETY_ENDPOINT, json=sheety_data_to_post, headers=sheety_header
    )

    # use this to print to terminal after your post request to confirm you are
    # sending what you think you're sending. If the response comes back with just
    # an id and nothing else, you missed something.
    print(post_sheety.text)

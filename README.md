# Workout Tracker

Track your workouts using natural language with the NutritionIX API and
Sheety.


## Usage
When the program is run, it will ask you what exercises you have performed. You
can answer in regular English. (eg. I ran 5 miles and biked 3 miles). The NutritionIX
API will convert your sentence into data including today's date, today's time, the
name of the exercise, the duration and the calories burned.

From there, the data will be posted to a Google sheet via Sheety.

1. You will need a Google Sheet set up prior to running the app.
2. You will need APIs to [NutritionIX](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.q0xuqqvrenf4) and 
[Sheety](https://sheety.co/)
3. In Sheety, you will need to enable GET and POST for your project.
4. Sensitive info like API keys are stored in a .env file and called with 
[Python-Dotenv](https://pypi.org/project/python-dotenv/)
5. You can load all imports via the requirements.txt using:
`pip install -r requirements.txt`
6. Sheet authentication is set to Bearer. See [docs](https://sheety.co/docs/authentication)
7. Change constant variables such as height, age, etc to your personal info.
8. Exercise data on line 35 is a dictionary of headers from your Google Sheet.
Note that the dictionary keys need to be lower case even if your sheet headers are
title case or all caps.





## License
[MIT](https://choosealicense.com/licenses/mit/)
from flask import Flask
import flask_monitoringdashboard as dashboard
from random import random

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random()
    if random_number < 0.2:
        raise Exception("Random error occurred!")
    elif random_number < 0.4:
        raise ValueError("Random value error occurred!")
    
    return 'this is the home page'

@app.route("/test")
def test():
    return 'this is the test page'

dashboard.bind(app) # Should be added after all endpoints have been defined
app.run()
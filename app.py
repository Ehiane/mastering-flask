# imports 
from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My app
app = Flask(__name__)


# this decorator allows you to route to the homepage ("/") --> root directory
@app.route("/")
def index():
    """First main page of our application"""
    return "Testing 123"

if __name__ in "__main__":
    app.run(debug=True)
# imports 
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My app
app = Flask(__name__) # acts like the hub/manager to all of the different pages.


# this decorator allows you to route to the homepage ("/") --> root directory
@app.route("/")
def index():
    """First main page of our application"""
    return render_template("index.html") # access the index.html file from the templates folder

if __name__ in "__main__":
    app.run(debug=True)
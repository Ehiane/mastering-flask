# imports 
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My app
app = Flask(__name__) # acts like the hub/manager to all of the different pages.
Scss(app) # allows us to use scss files in our templates folder

# database setup
# sqlalchemy is an ORM (Object Relational Mapper) that allows us to interact with the database using Python objects instead of SQL queries.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # path to the database file
db = SQLAlchemy(app) # allows us to use the database in our app


# this decorator allows you to route to the homepage ("/") --> root directory
@app.route("/")
def index():
    """First main page of our application"""
    return render_template("index.html") # access the index.html file from the templates folder

if __name__ in "__main__":
    app.run(debug=True)
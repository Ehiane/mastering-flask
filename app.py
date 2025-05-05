# imports 
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My app
app = Flask(__name__) # acts like the hub/manager to all of the different pages.
Scss(app) # allows us to use scss files in our templates folder

# database setup
# sqlalchemy is an ORM (Object Relational Mapper) that allows us to interact with the database using Python objects instead of SQL queries.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # path to the database file
db = SQLAlchemy(app) # allows us to use the database in our app


# Data class - Row of data
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True) # unique identifier for each task
    content = db.Column(db.String(100), nullable=False) # content of the task
    complete  = db.Column(db.Boolean, default=False) # whether the task is complete or not
    created  = db.Column(db.DateTime, default=datetime.now) # date and time the task was created

    def __repr__(self):
        return f"<Task {self.id}>"

# this decorator allows you to route to the homepage ("/") --> root directory
@app.route("/")
def index():
    """First main page of our application"""
    return render_template("index.html") # access the index.html file from the templates folder

# runner and debugger
if __name__ in "__main__":

    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
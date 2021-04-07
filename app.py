import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# To get hold of the database
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Setting up an instance of PyMongo and adding the app into the constructor method
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # checking if username already exists in the db
        user_exisiting = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # producing error message if user exists
        if user_exisiting:
            flash("Username already exists")
            return redirect(url_for("registration"))

        # data from the form will post acting as the post method
        registration = {
            "fname": request.form.get("fname").lower(),
            "sname": request.form.get("sname").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            # "cpassword": generate_password_hash(request.form.get("cpassword"))
        }
        mongo.db.users.insert_one(registration)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("registration.html")


# This tells the application where and how to run.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

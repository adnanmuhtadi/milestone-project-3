from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


"""
To get hold of the Database
"""

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

"""
Setting up an instance of PyMongo and adding the app into the constructor method
"""


mongo = PyMongo(app)


"""
Function to get the list of recepes from Mongo DB and display in the home page
"""


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("home.html", recipes=recipes)


@ app.route("/")
@ app.route("/get_my_recipes")
# Function to get the list of recepes from Mongo DB and display them in your personal list of recipes
def get_my_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("my_recipes.html", recipes=recipes)


@ app.route("/registration", methods=["GET", "POST"])
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
        if request.form.get("password") == request.form.get("confirm"):
            registration = {
                "fname": request.form.get("fname").capitalize(),
                "sname": request.form.get("sname").capitalize(),
                "email": request.form.get("email").lower(),
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
            }
            mongo.db.users.insert_one(registration)

            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))
        flash("Password does not match!")
    return render_template("registration.html")


@ app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        user_exisiting = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exisiting:
            # ensure hashed password matches user input
            if check_password_hash(
                    user_exisiting["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@ app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's fname from db
    fname = mongo.db.users.find_one(
        {"username": session["user"]})["fname"]

    if session["user"]:
        return render_template("profile.html", fname=fname)

    return redirect(url_for("login"))


@ app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@ app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "meal_name": request.form.get("meal_name"),
            "url_link": request.form.get("url_link"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "num_servings": request.form.get("num_servings"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_steps": request.form.get("recipe_steps"),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    # to pull the meal type names from the mongodb
    meals = mongo.db.meals.find().sort("meal_name", 1)
    # reloads user to add_recipe page
    return render_template("add_recipe.html", meals=meals)


@ app.route("/edit_username/<username>", methods=["GET", "POST"])
def edit_username(username):
    if request.method == "POST":
        submit = {
            "new_username": request.form.get("username"),
        }
        mongo.db.user.update({"_id": ObjectId(username)}, submit)
        flash("Task Successfully Updated")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("edit_username.html", username=username)

    return redirect(url_for("login"))


@ app.route("/edit_password/<username>", methods=["GET", "POST"])
def edit_password(username):
    if request.method == "POST":
        submit = {
            "new_password": request.form.get("password"),
        }
        mongo.db.user.update({"_id": ObjectId(username)}, submit)
        flash("Task Successfully Updated")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("edit_password.html", username=username)

    return redirect(url_for("login"))


# This tells the application where and how to run.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

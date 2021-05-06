from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING, ASCENDING
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env
import math

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
    amount_recipes = mongo.db.recipes.count()
    recipes_pp = 7
    current_recipe_page = int(request.args.get('current_recipe_page', 1))
    amount_pages = range(1, int(
        math.ceil(amount_recipes / recipes_pp)) + 1)
    recipes = mongo.db.recipes.find().sort([('_id', ASCENDING)]).skip(
        (current_recipe_page - 1)*recipes_pp).limit(recipes_pp)
    return render_template(
        "home.html", recipes=recipes, current_recipe_page=current_recipe_page, amount_pages=amount_pages, amount_recipes=amount_recipes)


"""
Function to get the list of recepes from Mongo DB and display on my recipe page
"""


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    search_results = mongo.db.recipes.find(
        {'$text': {'$search': query}}).count()
    result_message = f"Search Results"
    return render_template("home.html", recipes=recipes, search_results=search_results, result_message=result_message)


@app.route("/mysearch", methods=["GET", "POST"])
def mysearch():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    search_results = mongo.db.recipes.find(
        {'$text': {'$search': query}}).count()
    result_message = f"Search Results ({search_results})"
    return render_template("my_recipes.html", recipes=recipes, search_results=search_results, result_message=result_message)


"""
Function to get the list of recepes from Mongo DB and display on my recipe page
"""


@ app.route("/get_my_recipes")
# Function to get the list of recepes from Mongo DB and display them in your personal list of recipes
def get_my_recipes():
    recipes = mongo.db.recipes.find()
    amount_recipes = mongo.db.recipes.count()
    recipes_pp = 7
    current_recipe_page = int(request.args.get('current_recipe_page', 1))
    amount_pages = range(1, int(
        math.ceil(amount_recipes / recipes_pp)) + 1)
    recipes = mongo.db.recipes.find().sort([('_id', ASCENDING)]).skip(
        (current_recipe_page - 1)*recipes_pp).limit(recipes_pp)
    return render_template(
        "my_recipes.html", recipes=recipes, current_recipe_page=current_recipe_page, amount_pages=amount_pages, amount_recipes=amount_recipes)


"""
Function to get the user registered into Mongodb
1 - To check if the user exists in the db
2 - To display and error message if they already exist
3.1 - Checks if the password and confirm password match
3.2 - Added the rest of the form into the DB
4 - set up the User Sessional
5 - Error Message if the passwords dont match
"""


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

            # Setting up the User session and redirects the user to the profile page
            session["user"] = request.form.get("username").lower()
            return redirect(url_for("profile", username=session["user"]))
        flash("Password does not match!")
    return render_template("registration.html")


"""
Function to get the user logged in
1. Checks if the Username is registered in the DB
2. Checks if the username AND password is correct before logging in.
"""


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
            flash("Username can not be found")
            return redirect(url_for("login"))

    return render_template("login.html")


"""
Function to get the username set up and associated with the user session
"""


@ app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's fname from db
    fname = mongo.db.users.find_one(
        {"username": session["user"]})["fname"]

    if session["user"]:
        return render_template("profile.html", fname=fname)

    return redirect(url_for("login"))


"""
Function to close the session can have an error appear to inform the user
"""


@ app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


"""
Function to get the list of recepes from Mongo DB and display in the home page
"""


@ app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        to_share = "on" if request.form.get("to_share") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name").capitalize(),
            "meal_name": request.form.get("meal_name"),
            "url_link": request.form.get("url_link"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "num_servings": request.form.get("num_servings"),
            "recipe_ingredients": request.form.get("recipe_ingredients").splitlines(),
            "recipe_steps": request.form.get("recipe_steps").splitlines(),
            "is_it_veg": request.form.get("is_it_veg"),
            "to_share": request.form.get("to_share"),
            "created_by": session['user']
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_my_recipes"))

    # to pull the meal type names from the mongodb
    meals = mongo.db.meals.find().sort("meal_name", 1)
    # reloads user to add_recipe page
    return render_template("add_recipe.html", meals=meals)


@ app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        to_share = "on" if request.form.get("to_share") else "off"
        edit = {
            "recipe_name": request.form.get("recipe_name"),
            "meal_name": request.form.get("meal_name"),
            "url_link": request.form.get("url_link"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "num_servings": request.form.get("num_servings"),
            "recipe_ingredients": request.form.get("recipe_ingredients").splitlines(),
            "recipe_steps": request.form.get("recipe_steps").splitlines(),
            "is_it_veg": request.form.get("is_it_veg"),
            "to_share": request.form.get("to_share"),
            "created_by": session['user']
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_my_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # to pull the meal type names from the mongodb
    meals = mongo.db.meals.find().sort("meal_name", 1)
    # reloads user to add_recipe page
    return render_template("edit_recipe.html", recipe=recipe, meals=meals)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    all_recipe_info = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", all_recipe_info=all_recipe_info)


@ app.route("/edit_username/<username>", methods=["GET", "POST"])
def edit_username(username):
    if request.method == "POST":
        submit = {
            "new_username": request.form.get("username"),
        }
        mongo.db.users.update({"_id": ObjectId(username)}, submit)
        flash("username Successfully Updated")

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


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/delete_my_recipe/<recipe_id>")
def delete_my_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_my_recipes"))


# This tells the application where and how to run.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

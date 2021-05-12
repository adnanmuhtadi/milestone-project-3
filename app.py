import os
import math
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING, ASCENDING
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
Setting up an instance of PyMongo and adding
the app into the constructor method
"""


mongo = PyMongo(app)


"""
HomePage 
Function to get the list of recipes from Mongo DB and display in the home page
"""


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # Variables set for the recipes and amount of recipes
    recipes = list(mongo.db.recipes.find())
    amount_recipes = mongo.db.recipes.count()
    # The amount of recipes to be displayed per page
    recipes_pp = 5
    # Variable for the pagination and for it be displayed ascenting
    current_recipe_page = int(request.args.get('current_recipe_page', 1))
    amount_pages = range(1, int(
        math.ceil(amount_recipes / recipes_pp)) + 1)
    recipes = mongo.db.recipes.find().sort([('_id', ASCENDING)]).skip(
        (current_recipe_page - 1)*recipes_pp).limit(recipes_pp)

    # Rendering the home page and passing all the variables mentioned above
    return render_template(
        "home.html", recipes=recipes, current_recipe_page=current_recipe_page,
        amount_pages=amount_pages, amount_recipes=amount_recipes)


"""
Home Search Function
Function to get the list of recipes from Mongo DB and display on Home page
"""


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    # using the query to find the recipe
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    search_results = mongo.db.recipes.find(
        {'$text': {'$search': query}}).count()
    # displaying the results after the search has completed
    result_message = f"Search Results"

    # Rendering the home page and passing all the variables mentioned above
    return render_template(
        "home.html", recipes=recipes, search_results=search_results,
        result_message=result_message)


"""
Home Delete Recipe
Function to delete the recipes from Mongo DB
"""


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


"""
Registration Page
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
        # checking both password and confirm password match
        if request.form.get("password") == request.form.get("confirm"):
            registration = {
                "fname": request.form.get("fname").capitalize(),
                "sname": request.form.get("sname").capitalize(),
                "email": request.form.get("email").lower(),
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
            }
            mongo.db.users.insert_one(registration)

            # Setting up the User session and redirects the user
            # to the profile page
            session["user"] = request.form.get("username").lower()
            return redirect(url_for("profile", username=session["user"]))
        flash("Password does not match!")
    return render_template("registration.html")


"""
Login Page
Function to get the user logged in
1. Checks if the Username is registered in the DB
2. Checks if the username AND password is correct before logging in.
"""


@ app.route("/login", methods=["GET", "POST"])
def login():
    if 'user' in session:
        flash('You are already logged in')
        return redirect(url_for('profile', username=session["user"]))

    if request.method == "POST":
        # check if username exists in db
        user_exisiting = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exisiting:
            # ensure hashed password matches user input
            if check_password_hash(
                    user_exisiting["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("get_my_recipes"))
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
Profile Page
Function to get the username set up and associated with the user session
"""


@ app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    # grab the session user's fname from db
    fname = mongo.db.users.find_one(
        {"username": session["user"]})["fname"]

    return render_template("profile.html", fname=fname)


"""
Logout
Function to close the session can have an error appear to inform the user
"""


@ app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


"""
My Recipes Function
Function to get the list of recepes from Mongo DB and display on my recipe page
"""


@ app.route("/get_my_recipes")
def get_my_recipes():
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    # Function to get the list of recepes from Mongo DB and display
    # them in your personal list of recipes
    recipes = mongo.db.recipes.find()
    amount_recipes = mongo.db.recipes.count()
    # The amount of recipes to be displayed per page
    recipes_pp = 9
    # Variable for the pagination and for it be displayed ascenting
    current_recipe_page = int(request.args.get('current_recipe_page', 1))
    amount_pages = range(1, int(
        math.ceil(amount_recipes / recipes_pp)) + 1)
    recipes = mongo.db.recipes.find().sort([('_id', ASCENDING)]).skip(
        (current_recipe_page - 1)*recipes_pp).limit(recipes_pp)
    # Rendering the home page and passing all the variables mentioned above
    return render_template(
        "my_recipes.html", recipes=recipes,
        current_recipe_page=current_recipe_page,
        amount_pages=amount_pages, amount_recipes=amount_recipes)


"""
My Recipe Search Function
Function to get the list of recipes from Mongo DB and display on my recipe page
"""


@app.route("/mysearch", methods=["GET", "POST"])
def mysearch():
    query = request.form.get("query")
    # using the query to find the recipe
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    search_results = mongo.db.recipes.find(
        {'$text': {'$search': query}}).count()
    # displaying the results after the search has completed
    result_message = f"Search Results ({search_results})"

    # Rendering the my recipe page and passing all the variables mentioned above
    return render_template(
        "my_recipes.html", recipes=recipes,
        search_results=search_results, result_message=result_message)


"""
My Recipes Delete Function
Function to delete the recipes from Mongo DB
"""


@app.route("/delete_my_recipe/<recipe_id>")
def delete_my_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_my_recipes"))


"""
Add Recipe
Function to get the list of recepes from Mongo DB and display in the home page
"""


@ app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    # creates a dictionary and adds it to the recipe table within the database
    if request.method == "POST":
        to_share = "on" if request.form.get("to_share") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name").capitalize(),
            "meal_name": request.form.get("meal_name"),
            "url_link": request.form.get("url_link"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "num_servings": request.form.get("num_servings"),
            "recipe_ingredients": request.form.get(
                "recipe_ingredients").splitlines(),
            "recipe_steps": request.form.get("recipe_steps").splitlines(),
            "is_it_veg": request.form.get("is_it_veg"),
            "to_share": request.form.get("to_share"),
            "created_by": session['user']
        }
        # Inserts the recipe into the database
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        # redirects the user back to the my recipe page
        return redirect(url_for("get_my_recipes"))

    # to pull the meal type names from the mongodb
    meals = mongo.db.meals.find().sort("meal_name", 1)
    # reloads user to add_recipe page
    return render_template("add_recipe.html", meals=meals)


"""
View Recipes Function
Function to get the list of recepes from Mongo DB and display on my recipe page
"""


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    # finds the one recipe which is associated to the chosen ID
    all_recipe_info = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", all_recipe_info=all_recipe_info)


"""
Edit Recipe
Function to get the list of recepes from Mongo DB and display in the home page for it to updated
"""


@ app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Creates a dictionary and adds the recipe to the associated fields
        to_share = "on" if request.form.get("to_share") else "off"
        edit = {
            "recipe_name": request.form.get("recipe_name").capitalize(),
            "meal_name": request.form.get("meal_name"),
            "url_link": request.form.get("url_link"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "num_servings": request.form.get("num_servings"),
            "recipe_ingredients": request.form.get(
                "recipe_ingredients").splitlines(),
            "recipe_steps": request.form.get("recipe_steps").splitlines(),
            "is_it_veg": request.form.get("is_it_veg"),
            "to_share": request.form.get("to_share"),
            "created_by": session['user']
        }
        # Updates the recipe with usings its ID
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated")
        # redirects the user back to the my recipe page
        return redirect(url_for("get_my_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # to pull the meal type names from the mongodb
    meals = mongo.db.meals.find().sort("meal_name", 1)
    # reloads user to add_recipe page
    return render_template("edit_recipe.html", recipe=recipe, meals=meals)


"""
View Recipes Delete Function
Function to delete the recipes from Mongo DB
"""


@app.route("/delete_view_recipe/<recipe_id>")
def delete_view_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_my_recipes"))


"""
Edit Username 
Function to allow the logged in user to change the username
(using username as the parameter)
It will also update the recipes 'created by' field to the new username
"""


@ app.route("/edit_username/<username>", methods=["GET", "POST"])
def edit_username(username):
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Variable to find the current user session username
        # To change the created by to the new username
        # To find the recipes from the current user
        current_user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        created_by_change = {"created_by": request.form.get("new_username")}
        created_by_check = mongo.db.recipes.find(
            {'created_by': current_user})

        # If statment to check the libray of recipes with the username,
        # and if updates all the created by to the new username if true.
        if created_by_check:
            mongo.db.recipes.update_many(
                {"created_by": username},
                {"$set": created_by_change})

        # variables to check and change the username
        username_change = {"username": request.form.get("new_username")}
        check_username = mongo.db.users.find_one(
            {'username': request.form.get('new_username')})

        # Checks if they username has already been taken
        # if true, redirects to them to the username-change page
        if check_username:
            flash('This username is already taken,\
                Please enter a new different username')
            return redirect(url_for(
                'username_change', username=session["user"]))
        else:
            mongo.db.users.update_one(
                {"username": username}, {"$set": username_change})

        # loggs the user out for them to log back in
        flash("You have now been logged out, \
              as the username has been changed.\
              Please use your new username to login.")
        session.pop("user")
        return redirect(url_for("login"))

    return render_template("edit_username.html", username=session["user"])


"""
Edit password function 
Function to get the list of meal types from Mongo DB and display it
"""


@app.route("/edit_password/<username>", methods=["GET", "POST"])
def edit_password(username):
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Variable to find the current user session username
        # Variable to associate the form input fields to
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_new_password = request.form.get("confirm_new_password")

        # checks if the current password matches
        if check_password_hash(mongo.db.users.find_one(
                {'username': username})['password'], current_password):
            # checks if the new password and confirm password match
            if new_password == confirm_new_password:
                mongo.db.users.update_one(
                    {"username": username},
                    {"$set": {'password': generate_password_hash(
                        new_password)}})

                # logs the user out, to login again
                flash(
                    "You have been logged out, remember to use new password.")
                session.pop("user")
                return redirect(url_for("login"))

            else:
                # flash messages if any mistakes have occured.
                flash("Your new and confirm password do not match,\
                    Please try again")
                return redirect(url_for("edit_password",
                                        username=session["user"]))
        else:
            flash('Your Current password is incorrect,\
                Please try again')
            return redirect(url_for('edit_password', username=session["user"]))

    return render_template("edit_password.html", username=session["user"])


"""
Manage Meal Types  
Function to get the list of meal types from Mongo DB and display it
"""


@app.route("/get_meals")
def get_meals():
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    # gets the meal types and sorts them out by meal_name
    meals = list(mongo.db.meals.find().sort("meal_name", 1))
    return render_template("meals.html", meals=meals)


"""
Add Manage Meal Types  
Function to get the list of meal types from Mongo DB and display it
"""


@app.route("/add_meal", methods=["GET", "POST"])
def add_meal():
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # checking if meal type already exists in the db
        meal_exisiting = mongo.db.meals.find_one(
            {"meal_name": request.form.get("meal_name")})

        # producing error message if meal type exists
        if meal_exisiting:
            flash("Meal type already exists")
            return redirect(url_for("add_meal"))

        # creates a dictonary for the mean name
        meal = {
            "meal_name": request.form.get("meal_name")
        }

        # add the meal type to the database
        mongo.db.meals.insert_one(meal)
        flash("New Category Added")
        return redirect(url_for("get_meals"))

    return render_template("add_meal.html")


"""
Edit meal type function
Function to get the list of meal types from Mongo DB and display it
"""


@app.route("/edit_meal/<meal_id>", methods=["GET", "POST"])
def edit_meal(meal_id):
    # If statement to prevent non registered users to access the this part of the site
    if 'user' not in session:
        flash("You need to be logged in to access this page.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Creates a dictionary and adds the meal type to the associated field
        submit = {
            "meal_name": request.form.get("meal_name")
        }

        # Updates the meal type using its ID
        mongo.db.meals.update({"_id": ObjectId(meal_id)}, submit)
        flash("Meal Successfully Updated")
        # redirects the admin back to the manage meal type page
        return redirect(url_for("get_meals"))

    meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    # reloads user to edit_meal.html page
    return render_template("edit_meal.html", meal=meal)


"""
Delete meal type function
Function to delete the meal type from Mongo DB
"""


@app.route("/delete_meal/<meal_id>")
def delete_meal(meal_id):
    mongo.db.meals.remove({"_id": ObjectId(meal_id)})
    flash("Meal Successfully Deleted")
    return redirect(url_for("get_meals"))


"""
Error Handling Function
Function to handle error 404 and error 500
"""


@app.errorhandler(404)
def no_error_404(error):
    return render_template('error_404.html'), 404


@app.errorhandler(500)
def internal_server_error_404(error):
    return render_template('error_500.html'), 500


# This tells the application where and how to run.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

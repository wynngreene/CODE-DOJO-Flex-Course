from flask import render_template, redirect, session, request, flash
from flask_app import app
# from flask_app.models.user_Model import User
# from flask_bcrypt import Bcrypt        
# bcrypt = Bcrypt(app) 

# 00 ROUTES
@app.route("/")
def index():
    return render_template("index.html")

# 01 ROUTES
@app.route("/recipes")
def dashboard():
    return render_template("home.html")

# 02 ROUTES
@app.route("/recipes/new")
def new_recipe():
    return redirect("/recipes")

# 03 ROUTES
@app.route("/recipes/{id}")
def detail_recipe():
    return redirect("/recipes")

# 04 ROUTES
@app.route("/recipes/edit")
def edit_recipe():
    return redirect("/recipes")

# 05 ROUTES
@app.route("/recipes/edit")
def delete_recipe():
    return redirect("/recipes")
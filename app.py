# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import *


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def results():
    user_breakfast = request.form["breakfast"]
    user_name = request.form["nickname"]
    breakfast_rating = get_breakfast_rating(user_breakfast)
    return render_template("results.html", user_breakfast=user_breakfast, user_name=user_name, breakfast_rating=breakfast_rating)


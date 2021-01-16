# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
import model, bcrypt, random, time
from stellar_sdk import Server, Asset, Account, Keypair, TransactionBuilder, Network

# -- Initialization section --
app = Flask(__name__)

app.secret_key = "ojI3jkol:#Me]_mk2mkm@mMWr3"
user = os.environ['user']
pw = os.environ['pw']

# name of database
app.config['MONGO_DBNAME'] = 'HTN21'

# URI of database
app.config['MONGO_URI'] = f'mongodb+srv://{user}:{pw}@cluster0.6gvi8.mongodb.net/HTN21?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup', methods=["GET", "POST"])
def signup(): 
    return "To Do"

@app.route('/login', methods=["GET", "POST"])
def login(): 
    return "To Do"

@app.route('/explore')
def explore(): 
    return "To Do"

@app.route('/CreateFundraiser', methods=["GET","POST"])
def CreateFundraiser():
    return "To Do"

@app.route('/f/<fundraiser_id>')
def f(fundraiser_id):
    return "To Do"

@app.route('/donate/<fundraiser_id>', methods = ["GET","POST"])
def donate(fundraiser_id):
    return "To Do"

@app.route('/logout')
def logout():
    session.clear()
    return "To Do"

@app.route('/deleteAccount', methods=["GET","POST"])
def deleteAccount(): 
    return "To Do"

@app.route('/editProfile', methods=["GET","POST"])
def editProfile(): 
    return "To Do"

@app.route('/history')
def history(): 
    return "To Do"







# @app.route('/add')

# def add():
#     # connect to the database

#     # insert new data

#     # return a message to the user
#     return ""

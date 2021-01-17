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

# CONNECT TO DB, ADD DATA

@app.route('/signup', methods=["GET","POST"]) 
def signup():
    if session: 
        return redirect(url_for('/explore'))
    if request.method != "GET":
        user_name = request.form["fullName"] 
        user_email = request.form["email"]
        user_password = request.form["password"]
        user_public_key = request.form["publicKey"]
        if model.verify_destination(user_public_key) is False: 
            return "Your public key doesn't exist. Please try again"
        user_private_key = request.form["privateKey"]
        data_user_info = mongo.db.users
        user_info = data_user_info.find({})
        userData = []
        for i in user_info: 
            userData.append(i)
        existing_user = data_user_info.find_one({'email': user_email})
        if existing_user is None: 
            new_id = False
            user_id = 0
            while new_id is False: 
                random.seed(time.time())
                user_id = round(random.random()*10000000000)
                exists = data_user_info.find_one({'id':user_id})
                if exists is None:
                    new_id = True
            data_user_info.insert({"name":user_name, "email":user_email, "password": str(bcrypt.hashpw(user_password.encode("utf-8"), bcrypt.gensalt()), 'utf-8'),
            "public_key": user_public_key, "private_key": user_private_key, "id":user_id})
            session["user"] = user_id
            return redirect(url_for('explore'))
        else: 
            return 'That email already exists! Try logging in.'
    else: 
        return render_template('signup.html')

@app.route('/login', methods = ["GET","POST"])
def login(): 
    if session: 
        return redirect(url_for('explore'))
    if request.method != "GET": 
        user_email = request.form["email"]
        user_password = request.form["password"]
        data_user_info = mongo.db.users 
        user_info = data_user_info.find({})
        userData = []
        for i in user_info: 
            userData.append(i)
        login_user = data_user_info.find_one({'email': user_email}) 
        if login_user is None: 
            return ("It seems like you do not have an account. Please type your email correctly or sign up.")
        elif(user_email == login_user["email"]) and (bcrypt.hashpw(user_password.encode('utf-8'), login_user['password'].encode('utf-8')) == login_user["password"].encode('utf-8')):
            session["user"] = login_user['id']           
            return redirect(url_for('explore'))          
        return "Invalid combination! Please try again."
    else: 
        return render_template('login.html')

@app.route('/explore') 
def explore(): 
    fundraisers_info = mongo.db.fundraisers 
    fundraisers = fundraisers_info.find({})
    return render_template('explore.html', fundraisers=fundraisers)

@app.route('/CreateFundraiser', methods = ["GET","POST"])
def CreateFundraiser(): 
    if session:
        if request.method == "POST": 
            fundraisers = mongo.db.fundraisers
            title = request.form["title"]
            date = request.form["date"]
            description = request.form["description"]
            location = request.form["location"]
            category = request.form["category"] 
            # ADD AN ID GENERATOR
            new_id = False
            while new_id is False: 
                random.seed(time.time())
                id_fundraiser = round(random.random()*10000000000)
                exists = fundraisers.find_one({'id':id_fundraiser})
                if exists is None:
                    new_id = True
            fundraisers.insert({"title":title, "date":date, "description":description, 
                                "location":location, "category":category, "id":id_fundraiser,
                                "creator":session["user"]})
            return redirect(url_for('explore'))  
        else: 
            return render_template("CreateFundraiser.html")
    else: 
        return redirect(url_for('/login'))


@app.route('/f/<fundraiser_id>') 
def f(fundraiser_id):  
    fundraisers = mongo.db.fundraisers 
    f_id = int(fundraiser_id)
    fundraiser = fundraisers.find_one({'id':f_id}) 
    
    donations_all = mongo.db.donations
    donations = donations_all.find({'fundraiser':fundraiser_id}) 

    if not fundraiser: 
        return "Sorry, no profile. <a href='/explore'>Return to the explore page</a>"
    return render_template('f.html', **locals())

@app.route('/donate/<fundraiser_id>', methods = ["GET","POST"])
def donate(fundraiser_id): 
    if session: 
        fundraisers = mongo.db.fundraisers
        f_id = int(fundraiser_id)
        fundraiser = fundraisers.find_one({'id':int(f_id)})
        users = mongo.db.users 
        user = users.find_one({'id':int(session["user"])})
        if not user:
                return redirect(url_for('/login'))
        # return str(session['user'])
        if not fundraiser: 
            return "Sorry, no profile. <a href='/explore'>Return to the explore page</a>"
        
        if request.method == "POST": 
        
            donations = mongo.db.donations
            display_name = request.form["name"] 
            asset = request.form["asset"]  
            quantity = request.form["quantity"] 
            message = request.form["message"]  
            donator_id = session["user"] 

            donator_sKey = user['private_key']
            creator_fundraiser = users.find_one({'id':fundraiser['creator']})

            fundraiser_pKey = creator_fundraiser['public_key']

            if (model.sendPayment(donator_sKey, fundraiser_pKey, quantity, asset, message, str(donator_id), str(fundraiser['id'])) == False): 
                return "Sorry, the transaction failed. Please try again or check your assets."
            donations.insert({"display":display_name,"fundraiser":fundraiser_id,"donator":donator_id,
                                "asset":asset,"quantity":int(quantity),"message":message})
            return redirect(url_for('history'))
        else: 
            return render_template('donate.html', **locals()) 
    else: 
        return redirect(url_for('/login'))

@app.route('/logout')
def logout(): 
    session.clear() 
    return "Back to home page <a href='/index'>here</a>." 

@app.route('/deleteAccount', methods=["GET","POST"])
def deleteAccount(): 
    if session: 
        users = mongo.db.users 
        users.delete_one({"id":session["id"]})
        session.clear() 
        return "Your account has been deleted. Return to the home page <a href='/index'>here</a>"
    else: 
        return "You aren't signed in! If you would like to delete your account, please log in <a href='/login'>here!</a>"

@app.route('/editProfile', methods=["GET","POST"])
def editProfile(): 
    if session: 
        users = mongo.db.users
        user = users.find_one({"id":session["user"]})
        if not user: 
            return url_for('/login')
        else: 
            return "<h3> PAGE UNDER CONSTRUCTION, IF YOU NEED TO EDIT YOUR PROFILE PLEASE CONTACT US OR DELETE YOUR ACCOUNT <a href='/deleteAccount'>HERE</a>!!!!"

@app.route('/history')
def history(): 
    if session: 
        users = mongo.db.users
        user = users.find_one({"id":session["user"]})  
        donations_all = mongo.db.donations  
        donations = donations_all.find({})  
        fundraisers_all = mongo.db.fundraisers
        fundraisers = fundraisers_all.find({})
        my_fundraisers = []
        my_balances = []
        donated = []

        for fundraiser in fundraisers: 
            if(fundraiser['creator'] == user['id']):
                my_fundraisers.append([fundraiser['title'], fundraiser['id']]) # TAKES THE FUNDRAISERS THATY YOU CREATED

        for donation in donations:  
            for fundraiser in my_fundraisers: 
                if(int(donation['fundraiser']) == fundraiser[1]):  
                    for asset_type in my_balances:   
                        if(asset_type[0] == donation['asset']):   
                            asset_type[1]=str(int(donation['quantity'])+int(asset_type[1]))   
                        else: 
                            my_balances.append([donation['asset'],donation['quantity']])  
    
            if(donation['donator']==session['user']): 
                donated_fundraiser = fundraisers_all.find_one({'id':int(donation['fundraiser'])})  
                donated.append([donated_fundraiser['title'], donation['asset'], donation['quantity']]) #TAKES THE TITLE, ASSET TYPE, and QUANTITY 

        return render_template('history.html', **locals()) 
    else:  
        return render_template('index.html')         

# Working

# @app.route('/add')
# def add():
#     # connect to the database

#     # insert new data

#     # return a message to the user
#     return ""

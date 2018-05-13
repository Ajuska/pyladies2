# Domaci ukol

# 1. vyhledavani seznamu pomoci jmena a telefonu
# 2. vkladani noveho zanamu (jmeno, telefon)
# 3. mazani zanamu (nutno pouzit _id)

from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from faker import Faker
from bson.objectid import ObjectId

faker = Faker('cs_CZ')

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'list_of_phones'
mongo = PyMongo(app)


@app.route('/', methods=["GET", "POST"])
def index():
    phones = mongo.db.phones.find()
    #new_phone = mongo.db.phones.insert({"name": faker.name(), "phone": faker.phone_number()})
    return render_template('index_homework.html', phones=phones)

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        jmeno = request.form['jmeno']
        telefon = request.form['telefon']
        new_record = mongo.db.phones.insert({"name": jmeno, "phone": telefon})
        return redirect(url_for('index'))

    return render_template('add.html')
@app.route('/erase', methods=["GET", "POST"])
def erase():
    if request.method == "POST":
        phones = mongo.db.phones
        ID = request.form['ID']
        find_ID = phones.find_one({"_id": ObjectId(ID)})
        phones.remove(find_ID)
        return redirect(url_for('index'))

    return render_template('erase.html')

@app.route('/find', methods=["GET", "POST"])
def find():
    if request.method == "POST":
        phones = mongo.db.phones
        zadani = request.form['zadani']
        print(zadani)
        find_record = phones.find_one({"name": zadani})
        print(find_record)
        return render_template('find.html', find_record=find_record)
    return render_template('index_homework.html')

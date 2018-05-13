from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pyladies'
mongo = PyMongo(app)

@app.route('/')
def index():
    phones = mongo.db.phones.find()[:20]
    return render_template('list.html', phones=phones)

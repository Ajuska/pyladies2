from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.template_filter('capt')
def capitalize(word):
    return word[0].upper() + word[1:]

@app.route('/')
def index():
    return 'Ahoj PyLadies!'

@app.route('/url/')
def url():
    return url_for('hello', _external=True)

@app.route('/hello/')
@app.route('/hello/<name>/')
@app.route('/hello/<name>/<int:count>')
def hello(name='world', count=1):
    return render_template('hello.html', name=name)

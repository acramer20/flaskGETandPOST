from flask import Flask

app = Flask(__name__)


"""welcome page will return the msg welcome and so on for home and back"""
@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"
# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

"""adding a to b"""
@app.route('/add')
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)

"""subtracting b from a"""
@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)

    return str(result)

"""multiplying a times b"""
@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)

"""divide a by b"""
@app.route('/div')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

"""all in one"""
@app.route('/math/<operation>')
def calculate(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operation](a,b)
    return str(result)

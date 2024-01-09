#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print (string)
    return f'{string}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = list(range(parameter + 1))
    return render_template('count.html', numbers=numbers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

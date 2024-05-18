#!/usr/bin/python3
"""
Write a script that starts a Flask web application
check if n is odd or even: display a HTML page only
if n is an integer
"""
from flask import Flask
from flask import abort
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    if n.isdigit():
        return "{} is a number".format(n)
    return abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def is_number_template(n):
    if n.isdigit():
        return render_template("5-number.html", number=n)
    return abort(404)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_number_odd_or_even(n):
    value = "odd"
    if n % 2 == 0:
        value = "even"
    return render_template("6-number_odd_or_even.html", n=n, value=value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

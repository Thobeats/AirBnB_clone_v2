#!/usr/bin/python3
"""
Write a script that starts a Flask web application
check if n is odd or even: display a HTML page only
if n is an integer
"""
from flask import Flask
from flask import abort
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """
    removes current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def all_states():
    """
    A function to get a list of all
    the states
    """
    states = storage.all(State)
    stateValues = states.values()

    return render_template('7-states_list.html', states=stateValues)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

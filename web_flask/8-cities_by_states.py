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
from operator import attrgetter

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    A function to get a list of all
    the states
    """
    states = storage.all(State)
    state_values = states.values()
    states_final = sorted(state_values, key=attrgetter('name'))
    return render_template('8-cities_by_states.html',
            states=states_final)


@app.teardown_appcontext
def close(self):
    """
    removes current SQLAlchemy Session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

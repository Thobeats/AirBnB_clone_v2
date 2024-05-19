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


@app.route("/states", strict_slashes=False)
def all_states():
    """
    A function to get a list of all
    the states
    """
    states = storage.all(State)
    state_values = states.values()
    states_final = sorted(state_values, key=attrgetter('name'))

    return render_template('7-states_list.html', states=states_final)


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """
    A function to get a particular
    state by the id
    """
    states = storage.all(State)
    state = states["State.{}".format(id)]

    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_appcontext(self):
    """
    removes current SQLAlchemy Session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

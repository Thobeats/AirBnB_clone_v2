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
from models.amenity import Amenity
from models.place import Place
from operator import attrgetter

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def all_states():
    """
    A function that gets all the states
    and amenities
    """
    states = storage.all(State)
    state_values = states.values()
    states_final = sorted(state_values, key=attrgetter('name'))

    amenities = storage.all(Amenity)
    amenity_values = amenities.values()
    amenities_final = sorted(amenity_values, key=attrgetter('name'))

    places = storage.all(Place)
    place_values = places.values()
    places_final = sorted(place_values, key=attrgetter('name'))

    return render_template('100-hbnb.html', states=states_final,
                           amenities=amenities_final,
                           places=places_final)


@app.teardown_appcontext
def teardown_appcontext(self):
    """
    removes current SQLAlchemy Session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

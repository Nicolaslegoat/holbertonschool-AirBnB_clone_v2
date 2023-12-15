#!/usr/bin/python3
"""Script that starts a Flask web application. """


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all State objects in DBStorage"""
    states = storage.all(State)

    return render_template("9-states.html",
                           states=states, current_route="route_states")


@app.route("/states/<id>", strict_slashes=False)
def cities_of_states():
    list_states = storage.all(State)
    for state in list_states.values():
        if state.id == id:
            cities = state_cities

            return render_template("9-states.html", states=list_states,
                                   cities=cities, state=state,
                                   current_route="route_cities")
    return render_template("9-states.html", current_route="not found")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

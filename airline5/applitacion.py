# import os
# import config

from flask import Flask, render_template, request, jsonify
from models import *

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger.
    # passenger = Passenger(name=name, flight_id=flight_id)
    # db.session.add(passenger)
    # db.session.commit()
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    
    # Get all passengers.
    # passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    # we change the above line for this (because we add new line about relationships in models.py)
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        # return render_template("error.html", message="No such flight.")
        return jsonify({"error":"Invalid flight id."}), 422

    
    # Get all passengers.
    # passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    # we change the above line for this (because we add new line about relationships in models.py)
    passengers = flight.passengers
    # return render_template("flight.html", flight=flight, passengers=passengers)
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })

if __name__ == "__main__":
    app.run(debug=True)



import os
import config

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_pyfile('config.py')
db.init_app(app)

def main():
    # flights = Flight.query.all()
    # flights = Flight.query.filter(Flight.duration > 300).order_by(Flight.origin.desc()).all()
    # flights = Flight.query.filter(Flight.origin.in_(["Tokyo","Paris"])).order_by(Flight.origin.desc()).all()
    # flights = Flight.query.filter(Flight.duration > 300).all()
    # flights = Flight.query.order_by(Flight.origin.desc()).all()
    flights = db.session.query(Flight, Passenger)\
        .filter(Flight.id == Passenger.flight_id)\
        .add_columns(Flight.origin, Flight.destination, Flight.duration, Passenger.name)\
        .order_by(Flight.id)\
        .all()
    for flight in flights:
        # print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.)
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes - Passenger Name: {flight.name}.")

if __name__ == "__main__":
    with app.app_context():
        main()
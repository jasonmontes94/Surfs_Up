# Pandas dependencies
import datetime as dt
import numpy as np
import pandas as pd
import os

# SQLite Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Import flask
from flask import Flask, jsonify

# Access SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into classes
Base = automap_base()

# Reflect the database results
Base.prepare(engine, reflect=True)

# Save the references
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to Database
session = Session(engine)

# Create a new flask instance
app = Flask(__name__)

# Create the starting point/root function (welcome route)
# create a function that directs investors where to go
@app.route('/')
def welcome():
    return('''
    
    Welcome to the Climate Analysis API! <br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end'''
    )
    
# Create the Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# #Create the precipitation function
# def precipitation():
#     # Date 1yr from most recent
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     # Date and precepitation from previous year
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return jsonify(precip) # Turn file into a .json file

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Provide both start and end route dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
# http://127.0.0.1:5000/api/v1.0/temp/start/end%20route

if __name__ == '__main__':
    app.run(debug=False)
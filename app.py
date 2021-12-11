#import the dependency
import datetime as dt

import numpy as np
import pandas as pd
import sqlalchemy
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the db
Base = automap_base()
Base.prepare(engine, reflect=True)

#save as references
Measurement = Base.classes.measurement 
Station = Base.classes.station 

#create a session link
session = Session(engine)

#create a new flask app instance
app = Flask(__name__)

#create first flask route
@app.route("/")
def welcome():
    return (
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#create second route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#create third route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    
# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)

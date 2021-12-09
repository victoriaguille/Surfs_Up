

#import the dependency
from flask import Flask, jsonify 
import datetime as dt
import numpy as np 
import pandas as pd 
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func 

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
def hello_world():
    return "Hello World"
# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)

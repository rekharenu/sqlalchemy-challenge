# Import the dependencies.
# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
import pandas as pd
import re
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine,func
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import session
from flask import Flask,jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# Declare a Base using `automap_base()`
Base= automap_base
# Use the Base class to reflect the database tables
Base.Prepare(autoload_with=engine)


# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station



# Create a session
session= session(engine)

#################################################
# Flask Setup
#################################################

app=Flask(__name__)



#################################################
# Flask Routes
#################################################
@aap.route("/")
def welcome():
    return(
        f"welcome to Hawaii Climate Analysis API!<br/>"
        f"Available Route:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start(enter in YYYY-MM-DD)<br/>"
        f"/api/v1.0/end(enter the YYYY-MM-DD)<br/>"
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    session= Session(engine)
    one_year = dt.date(2017,8,23)-dt.timedelta(days=365)
    last_year_date= dt.date(one_year.year,one_year.month,one_year.day)
    score= session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>=last_year_date).order_by(Measurement.date.desc()).all()
    p_dict= dict(score)
    print(f"precipitation - {p_dict}")
    print(f"precipitation section")
    return jsonify(p_dict)
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    select= [Station.station,Station.name,Station.latitude,Station.elevation]
    queryres= session.query(*select).all()
session.close()

stations=[]
for station,name,latu,longu,elev in queryres:
    station_dict={}
    station_dict["Station"]= station
    station_dict["Name"]=name
    station_dict["Latu"]= latu
    station_dict["Longu"]= longu
    station_dict["Elevelation"]= elev
    stations.append(station_dict)
    return jsonify(stations)
@app.route("/api/v1.0/tobs")
def tobs():
    session = Sessions(engine)
    queryresults= session.query(Measurement.date,Measurement.tobs).filter(Measurement.station== 'USC00519281')\
    .filter(Measurement.date>= '2016-08-23').all()
    tobs_obbser=[]
    for date, tobs in queryresults:

         tobs_dict={}
         tobs_dict["Date"]= date
         tobs_dict["Tobs"]= tobs
         tob_obbser.append(tobs_dict)

         return jsonify(tobs_obbser)
    
    @app.route("/api/v1.0/<start>")

    def get_tem_start(start):
        session= Session(engine)
        result_temp= session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date>=start).all()
        session.close()
        tempser=[]
        for min_temp,max_temp,avg_temp in result_temp:
            tempser_dict={}
            tempser_dict['Minimum Temp']= min_temp
            tempser_dict['Max Temp']= max_temp
            tempser_dict['Average Temp']= avg_temp
            tempser.append(tempser_dict)
            return jsonify(tempser)
        
        @app.route("/api/v1.0/<start>/<end>")
        def get_temp_end(start,end):
            session= Session(engine)
            result_end= session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
            filter(Measurement.date>=start).filter(Measurement.date<=end).all()
            session.close()

            tempser = []
            for min_temp,avg_temp,max_temp in result_temp:
                tempser_dict={}
                tempser_dict['Minim Temerature']= min_temp
                tempser_dict['Maxmin Temperature']= max_temp
                tempser_dict['avgerage Temperature']= avg_temp
                return jsonify(tempser_dict)
            
            if  __name__=='__main__':
                app.run(debug=True)








#################################################
# Flask Routes
#################################################

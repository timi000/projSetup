from models import create_classes
import os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)



#################################################
# Database Setup
#################################################


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///Covid_Vision.sqlite"
engine =app.config['SQLALCHEMY_DATABASE_URI'] 
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Covid_Vision = create_classes(db)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trends")
def trends():
    return render_template("trends.html")

@app.route("/choropleth")
def choropleth():
    return render_template("choropleth.html")        
    
@app.route("/api/v1.0/covid_trends")
def trend():
    Result=db.session.query( Covid_Vision[0].date, Covid_Vision[0].Mask,Covid_Vision[0].CERB, Covid_Vision[0].Patio,
    Covid_Vision[0].Zoom, Covid_Vision[0].Bike, Covid_Vision[0].numconf, Covid_Vision[0].numtestedtoday,
    Covid_Vision[0].numtoday,Covid_Vision[0].numdeathstoday, Covid_Vision[0].numactive
    )
  

    trd_list=[]
    for date, Mask, Zoom, CERB, Patio, Bike, numconf, numtestedtoday, numtoday , numdeathstoday , numactive in Result: 
        start_dict={}
        start_dict["date"]=date
        start_dict["Mask"]=Mask
        start_dict["Zoom"]=Zoom
        start_dict["CERB"]=CERB
        start_dict["Patio"]=Patio
        start_dict["Bike"]=Bike
        start_dict["confirmed cases"]=numconf
        start_dict["daily_tests"]=numtestedtoday
        start_dict["daily_cases"]=numtoday
        start_dict["active_cases"]=numactive
        start_dict["daily_deaths"]=numdeathstoday
        trd_list.append(start_dict) 
 
    return jsonify(trd_list)

 
   


@app.route("/api/v1.0/canada_covid")
def corona():
    Result=Result=db.session.query(Covid_Vision[1].date, Covid_Vision[1].prname,Covid_Vision[1].latitude, Covid_Vision[1].longitude, Covid_Vision[1].population, 
    Covid_Vision[1].numrecover, Covid_Vision[1].numrecoveredtoday,
    Covid_Vision[1].numconf, Covid_Vision[1].numtestedtoday,
    Covid_Vision[1].numtoday, Covid_Vision[1].numdeathstoday, Covid_Vision[1].numactive)
   

   
    cvd_list=[]
    for date, prname, latitude,longitude, population, numrecover, numrecoveredtoday,numconf, numtestedtoday, numtoday, numdeathstoday, numactive  in Result: 
        covid_dict={}
        covid_dict["date"]=date
        covid_dict["province_name"]=prname
        covid_dict["latitude"]=latitude
        covid_dict["longitude"]=longitude
        covid_dict["pop_size"]=population
        covid_dict["total_recoverd"]=numrecover
        covid_dict["total_recovered_today"]=numrecoveredtoday
        covid_dict["confirmed cases"]=numconf
        covid_dict["daily_tests"]=numtestedtoday
        covid_dict["daily_cases"]=numtoday
        covid_dict["active_cases"]=numactive
        covid_dict["daily_deaths"]=numdeathstoday

        cvd_list.append(covid_dict) 
 
    return jsonify(cvd_list)

   

if __name__ == '__main__':
    app.run(debug=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .getClinicalData import getClinicalData
from .getHealthBehaviors import getHealthData
from .getRegualtedIndustryData import get_regulated_industries_data
from .ObjectiveScore import getOverallObjectiveScore, getFeatureScore
from .PerceptionScore import get_sentiment_score
from .getCrimeData import get_crime_data
from .getHealthData import get_health_data

import pandas as pd
import os

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

years = ["2018", "2019", "2020", "2021", "2022"]
excel_data = []

for year in years:
    rankings_path = os.path.join(os.getcwd(), 'app/data/' + year + ' County Health Rankings Data.xlsx')
    excel_data.append(pd.read_excel(rankings_path ,sheet_name = 3,header=1))


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to the RHAIN server"}


@app.get("/clinical-care")
def get_county_info(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = getClinicalData(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/health-behavior")
def get_county_info(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = getHealthData(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/regulated-industries")
def get_regulated_industry_data_fuction(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = get_regulated_industries_data(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/crime")
def get_crime_data_function(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = get_crime_data(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/health")
def get_health_data_function(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = get_health_data(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

#----------------------------------------------------------------------------------------

@app.get("/feature-score")
def get_feature_score(state_name: str, county_name: str):
    # http://localhost:8000/feature-score?state_name=California&county_name=Marin
    # Filter the rows by county
    data = []
    for feature_name in ["Primary Care Physicians Rate","Average Number of Physically Unhealthy Days", "% Vaccinated","% With Access to Exercise Opportunities","% Uninsured","Preventable Hospitalization Rate","Years of Potential Life Lost Rate","Food Environment Index"]:        
        data.append(getFeatureScore(state_name, county_name, feature_name))
    # Convert the selected data to a dictionary and return it
    return data


@app.get("/health-score")
def get_county_info(state_name: str, county_name: str):
    # http://localhost:8000/health-score?state_name=California&county_name=Marin
    # Filter the rows by county
    data = getOverallObjectiveScore(state_name, county_name)
    # Convert the selected data to a dictionary and return it
    return data

@app.get("/perception-score")
def get_perception_score(state_name: str, county_name: str):
    # http://localhost:8000/perception-score?state_name=California&county_name=Los%20Angeles
    data = get_sentiment_score(state_name, county_name)
    return data
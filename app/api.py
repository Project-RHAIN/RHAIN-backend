from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.dataAPI.getClinicalData import getClinicalData
from app.dataAPI.getHealthBehaviors import getHealthData
from app.dataAPI.getRegualtedIndustryData import get_regulated_industries_data
from .ObjectiveScore import getOverallObjectiveScore, getFeatureScore, getCompareScore
from .PerceptionScore import get_sentiment_score
from app.dataAPI.getCrimeData import get_crime_data
from app.dataAPI.getHealthData import get_health_data
from app.dataAPI.getRegionalData import get_regional_data
from pydantic import BaseModel
from google.auth import jwt

from app.dataAPI.getMapVisData import getMapVisData


import pandas as pd
import os

app = FastAPI()

class CredentialRequest(BaseModel):
    clientId: str
    credential: str

class UserResponse(BaseModel):
    email: str
    first_name: str
    last_name: str
    picture: str

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

############################################################################################
# Init

years = ["2018", "2019", "2020", "2021", "2022"]
excel_data = []

for year in years:
    rankings_path = os.path.join(os.getcwd(), 'app/data/' + year + ' County Health Rankings Data.xlsx')
    excel_data.append(pd.read_excel(rankings_path ,sheet_name = 3,header=1))

regional_data_path = os.path.join(os.getcwd(), 'app/data/Population_Income_Area_2022.xlsx')
regional_data_excel = pd.read_excel(regional_data_path)

############################################################################################
# Home
############################################################################################
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to the RHAIN server"}

@app.get("/api", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to the RHAIN server API"}

############################################################################################
# Google Verify
############################################################################################
@app.post("/api/verifyGoogle")
def process_credential(credential_request: CredentialRequest):
    # Assuming you have some logic to process the credential request and retrieve user data
    claims = jwt.decode(credential_request.credential, verify=False)    
    email = claims['email']
    first_name = claims['given_name']
    last_name = claims['family_name']
    picture = claims['picture']
    # print("DECODED", claims)
    user_response = UserResponse(email=email, first_name=first_name, last_name=last_name, picture=picture)
    return user_response

############################################################################################
# Regional Data API
############################################################################################

@app.get("/api/regional-data")
def get_regional_data_function(state_name: str, county_name: str):
    # Filter the rows by county
    data = get_regional_data(state_name, county_name, regional_data_excel)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')
############################################################################################
# Visualization Data APIs
############################################################################################

@app.get("/api/clinical-care")
def get_county_info(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = getClinicalData(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/api/health-behavior")
def get_county_info(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = getHealthData(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/api/regulated-industries")
def get_regulated_industry_data_function(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = get_regulated_industries_data(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/api/crime")
def get_crime_data_function(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = get_crime_data(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

@app.get("/api/health")
def get_health_data_function(state_name: str, county_name: str, trend: bool):
    # Filter the rows by county
    data = get_health_data(state_name, county_name, excel_data, years, trend)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')

############################################################################################
# Map Data APIs
############################################################################################

@app.get("/api/map-vis")
def get_map_vis(state_name: str, map_vis: str):
    data = getMapVisData(state_name, mapVis=map_vis, excel_data=excel_data)
    return data.to_dict(orient='records')

############################################################################################
# Score APIs
############################################################################################

@app.get("/api/feature-score")
def get_feature_score(state_name: str, county_name: str):
    # http://localhost:8000/feature-score?state_name=California&county_name=Marin
    # Filter the rows by county
    data = []
    for feature_name in ["Primary Care Physicians Rate","Average Number of Physically Unhealthy Days", "Years of Potential Life Lost Rate","Food Environment Index","% Vaccinated","% With Access to Exercise Opportunities","% Uninsured","Preventable Hospitalization Rate"]:        
        data.append(getFeatureScore(state_name, county_name, feature_name))
    # Convert the selected data to a dictionary and return it
    return data

@app.get("/api/compare-score")
def get_compare_score(state_name: str, county_name: str):
    # http://localhost:8000/compare-score?state_name=California&county_name=Marin
    # Filter the rows by county
    data = []
    for feature_name in ["Education","Employment","Income","Health Behaviors","Physical Environment"]:        
        data.append(getCompareScore(state_name, county_name, feature_name))
    # Convert the selected data to a dictionary and return it
    return data


@app.get("/api/health-score")
def get_county_info(state_name: str, county_name: str):
    # http://localhost:8000/health-score?state_name=California&county_name=Marin
    # Filter the rows by county
    data = getOverallObjectiveScore(state_name, county_name)
    # Convert the selected data to a dictionary and return it
    return data

@app.get("/api/perception-score")
def get_perception_score(state_name: str, county_name: str):
    # http://localhost:8000/perception-score?state_name=California&county_name=Los%20Angeles
    data = get_sentiment_score(state_name, county_name)
    return data
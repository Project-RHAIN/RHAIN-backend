from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .getClinicalData import getClinicalData
from .ObjectiveScore import getOverallObjectiveScore, getFeatureScore

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


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to the RHAIN server"}


@app.get("/clinical-care")
def get_county_info(state_name: str, county_name: str):
    # Filter the rows by county
    data = getClinicalData(state_name, county_name)
    # Convert the selected data to a dictionary and return it
    return data.to_dict(orient='records')


@app.get("/feature-score")
def get_feature_score(state_name: str, county_name: str, feature_name: str):
    # http://localhost:8000/feature-score?state_name=California&county_name=Marin&feature_name=% Fair or Poor Health
    # Filter the rows by county
    data = getFeatureScore(state_name, county_name, feature_name)
    # Convert the selected data to a dictionary and return it
    return data


@app.get("/health-score")
def get_county_info(state_name: str, county_name: str):
    # http://localhost:8000/health-score?state_name=California&county_name=Marin
    # Filter the rows by county
    data = getOverallObjectiveScore(state_name, county_name)
    # Convert the selected data to a dictionary and return it
    return data
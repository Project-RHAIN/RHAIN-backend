from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.getClinicalData import getClinicalData

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
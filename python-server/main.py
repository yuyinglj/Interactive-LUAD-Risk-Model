from typing import Optional, List
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from model import run_model_creation


# App init
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


data_df = pd.read_csv("../data/model_input_data.csv")
print("Data loaded.")

# Data types
class SentItem(BaseModel):
    classifier_name: str
    prediction_type: str
    genelist: List[str] 
    day_thresh: int


# App routes
@app.post("/model")
def model_endpt(request_param: SentItem):
    res = run_model_creation(data_df,
                             request_param.classifier_name,
                             request_param.prediction_type,
                             request_param.genelist,
                             request_param.day_thresh) 

    return res

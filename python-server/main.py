from typing import Optional, List
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import create_model

### App init
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Data types
class SentItem(BaseModel):
    model_type: str
    genes: List[str]  # how to turn this into array?


## App routes
@app.post("/model")
def model_endpt(req_item: SentItem):
    res = create_model(req_item.model_type, req_item.genes)

    return res
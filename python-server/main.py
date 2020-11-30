from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

# App init
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origin_regex='(https://localhost:*)|(http://localhost:*)',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data types from requestor
class ExItem(BaseModel):
    name: str
    description: Optional[str] = None

class SentItem(BaseModel):
    model_type: str
    genes: Optional[str] = None # how to turn this into array?


# Routes
@app.get("/")
def read_root():
    return {"Hi": "You've hit the root"}


@app.get("/delay/{item_id}")
def delay_endpt(item_id: int, q: Optional[str] = None):
    print("got request, sleeping now")
    time.sleep(1)
    return {"item_id": item_id, "q": q}

@app.post("/model")
async def model_endpt(item: SentItem):
    # Get genes and model type out of request
    
    # train model with these genes

    # send response
    return item
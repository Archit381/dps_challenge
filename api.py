import pandas as pd
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware 
from routers.Prediction.prediction_route import router as predict_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(predict_router)

@app.get('/')
def _default_router():
    return Response('Server is running!')

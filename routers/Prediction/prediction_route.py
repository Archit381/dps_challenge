from fastapi import APIRouter
from pydantic import BaseModel
from utils.ProcessingClass import PreProcessingClass
import pickle

class RequestType(BaseModel):
    MONATSZAHL: str
    AUSPRAEGUNG: str
    JAHR: int
    MONAT: str

router = APIRouter(prefix='/predict')

global encoder, xgb_model

@router.on_event('startup')
def _loadPickleFiles():

    with open("lib\encoder.pkl", 'rb') as file:
        global encoder
        encoder = pickle.load(file)

    with open("lib\model.pkl", 'rb') as file:
        global xgb_model
        xgb_model = pickle.load(file)

    print("Pickle Files Loaded. Ready for Inference!")

def _do_inference(df):

    global xgb_model

    return xgb_model.predict(df)


@router.post("/")
def predict(data: RequestType):

    global encoder

    pc = PreProcessingClass(
        MONATSZAHL = data.MONATSZAHL,
        AUSPRAEGUNG = data.AUSPRAEGUNG,
        JAHR = data.JAHR,
        MONAT = data.MONAT,
        encoder = encoder
    )

    date_processed_df = pc._convert_date()

    final_df = pc._one_hot(date_processed_df)

    results = _do_inference(final_df)

    return {"Final Predictions": results.tolist()[0]}

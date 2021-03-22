import models.regressor as reg
from fastapi import FastAPI, Body
from joblib import load
from models.housing import Housing
import pandas as pd

app = FastAPI(title="House Price Prediction Model",
              description="API for California house prices",
              version="1.0")


@app.on_event('startup')
async def load_model():
    reg.model = load('models/rf_v1.joblib', )

@app.post('/predict', tags=["prediction"])
async def get_prediction(housing: Housing):
    housing = dict(housing)
    data = pd.DataFrame([housing.values()], columns=housing.keys())
    print(data)
    predictions = reg.model.predict(data).tolist()
    return {
        "predictions": predictions
    }


import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

model = joblib.load("model/model.pkl")
class_names = ["setosa", "versicolor", "virginica"]

app = FastAPI()

class IrisFeatures(BaseModel):
    features: List[float]

@app.get("/")
def root():
    return {"message": "API funcionando!"}

@app.post("/predict")
def predict(data: IrisFeatures):
    if len(data.features) != 4:
        raise HTTPException(status_code=400, detail="Precisa de 4 números")
    
    input_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    probabilities = model.predict_proba(input_array)[0]
    
    return {
        "classe": class_names[prediction],
        "probabilidades": {
            class_names[i]: round(float(p), 4)
            for i, p in enumerate(probabilities)
        }
    }
    

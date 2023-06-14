from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
app = FastAPI()

class CustomData(BaseModel):
    Age: int
    Gender: str
    Height: int
    Weight: int
    BMI: float

model = pickle.load(open("model3.pkl","rb"))

@app.post("/")
async def scoring_endpoint(data:CustomData):
    dic = {1:"Obese",0:"Normal Weight",2:"Over Weight",3:"Under weight"}
    df = pd.DataFrame([data.dict().values()],columns=data.dict().keys())
    df.Gender = df['Gender'].apply(lambda x: 1 if x=="Male" else 0)
    pred = model.predict(df)
    return {"Category":dic[int(pred[0])]}
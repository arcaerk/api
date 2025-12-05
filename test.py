from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()



@app.get("/raghav/xyz")#avaliable to world(not secure)
def add(a:int,b:int):
    return a+b

class subtractmodel(BaseModel):
    a:int
    b:int


def subtract(a:int,b:int):
    return a-b

@app.post("/subtract")#not available to world,first validate with pydantic to display
def subtract_numbers(model:subtractmodel):
    return subtract(model.a,model.b)

print(add(3,4))
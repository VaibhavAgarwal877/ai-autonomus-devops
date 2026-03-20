from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI DevOps Running"}

@app.get("/health")
def health():
    if random.randint(1,5) == 3:
        return {"status": "error"}
    return {"status": "ok"}
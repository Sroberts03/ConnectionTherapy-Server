from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to ConnectionTherapy API"}

@app.get("/health")
def read_root():
    return {"status": "ok"}
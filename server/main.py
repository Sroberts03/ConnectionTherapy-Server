from fastapi import FastAPI
from v1.api import api_router
from v1.global_exception_handler import add_exception_handlers

app = FastAPI()
app.include_router(api_router)
add_exception_handlers(app)

@app.get("/")
def read_root():
    return {"message": "Welcome to ConnectionTherapy API"}

@app.get("/api/v1/error")
async def trigger_error():
    raise Exception("This is a test error")
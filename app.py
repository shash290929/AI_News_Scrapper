from fastapi import FastAPI
from service_layer import llm_service
app = FastAPI()

@app.get("/kickoff")
def first_api():
    return llm_service()
from fastapi import FastAPI
from routes import insights

app = FastAPI(title="Brooder API")

app.include_router(insights.router)

@app.get("/")
def root():
    return {"message": "Welcome to Brooder API 🚀"}

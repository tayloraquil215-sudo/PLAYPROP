from fastapi import FastAPI
from db import Base, engine
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sports Betting Tracker")
app.include_router(router)

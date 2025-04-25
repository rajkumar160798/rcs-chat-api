# backend/main.py
from fastapi import FastAPI
from routes import rcs_router

app = FastAPI(title="RCS Chat API", version="1.0")

app.include_router(rcs_router, prefix="/api")

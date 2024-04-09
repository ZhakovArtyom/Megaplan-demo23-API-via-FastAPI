from fastapi import FastAPI
from src.routers.router import router as login_router


app = FastAPI(title="MegaplanAPI")
app.include_router(login_router)

from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import FileResponse
from src.crm_interaction.init import megaplan_client

router = APIRouter()


@router.get("/")
async def root():
    return FileResponse("src/templates/index.html")


@router.post("/login/")
async def login(login: str = Form(...), password: str = Form(...)):
    if (login, password) == await megaplan_client.get_credentials():
        return {"message": f"Привет, {await megaplan_client.get_username()}!"}
    else:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return templates.TemplateResponse("index.html", {"request": request, "current_datetime": current_datetime})


@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "user" and password == "password":
        return templates.TemplateResponse("welcome.html", {"request": request, "username": username})
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

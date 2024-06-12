from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse("index.html",
                                      {"request": request, "current_datetime": current_datetime})


@app.get("/time-difference/", response_class=HTMLResponse)
async def calculate_time_difference(request: Request, time_str: str):
    try:
        user_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()
        time_difference = current_time - user_time
        return templates.TemplateResponse("time_difference.html",
                                          {"request": request, "time_difference": time_difference})
    except ValueError:
        return templates.TemplateResponse("time_difference.html",
                                          {"request": request, "error_message": "Invalid time format. Please provide time in the format 'YYYY-MM-DD HH:MM:SS'."})
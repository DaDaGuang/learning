from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

expenses = []

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "expenses": expenses})

@app.post("/add")
def add_expense(amount: float = Form(...), category: str = Form(...)):
    expenses.append({
        "amount": amount,
        "category": category,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return {"message": "Added"}


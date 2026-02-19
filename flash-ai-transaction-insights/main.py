from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from insight_engine import generate_insight

app = FastAPI(title="Flash AI Transaction Insight Assistant")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "insight": None}
    )

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_transaction(request: Request):
    form = await request.form()

    insight = generate_insight(
        amount_sats=int(form["amount_sats"]),
        fee_sats=int(form["fee_sats"]),
        confirmation_time=int(form["confirmation_time_minutes"]),
        network=form["network"]
    )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "insight": insight}
    )

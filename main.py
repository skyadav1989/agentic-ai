import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from agents import ParallelAgent, SequentialAgent, LoopAgent
from memory import MemoryBank
from session import SessionService

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

parallel_agent = ParallelAgent()
sequential_agent = SequentialAgent()
loop_agent = LoopAgent()

memory = MemoryBank()
sessions = SessionService()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})




@app.post("/run")
async def run_agent(user_input: str = Form(...), agent_type: str = Form(...)):

    if agent_type == "parallel":
        result = await parallel_agent.run(user_input)
    elif agent_type == "sequential":
        result = await sequential_agent.run(user_input)
    else:
        result = await loop_agent.run(user_input)

    return JSONResponse(result)

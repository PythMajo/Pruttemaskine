from random import random

from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pathlib
import random
from pruttemaskine import play_sound, select_random_sound

app = FastAPI()

templates = Jinja2Templates(directory="templates")
sounds = list(pathlib.Path("./farts").iterdir())


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/fart")
async def fart():
    sound = select_random_sound(sounds)
    result = play_sound(sound)
    return result

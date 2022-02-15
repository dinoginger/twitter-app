"""
Lab 2-3
Marko Ruzak CS-1

Simple web application which uses TwitterAPI
and Leaflet.js to map given users' locations on map.
"""
import fastapi
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")

@app.get("/")
def something():
    return {"something"}


@app.get('/index/{name}', response_class=HTMLResponse)
async def read_item(request: fastapi.Request, name: str):
    return templates.TemplateResponse('index.html', {'request': request, 'name': name})
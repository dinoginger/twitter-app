"""
Lab 2-3
Marko Ruzak CS-1

Simple web application which uses TwitterAPI
and Leaflet.js to map given users' locations on map.
"""
import fastapi
import jinja2
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = fastapi.FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def something():
    response = RedirectResponse("/input")
    return response


@app.get('/input', response_class=HTMLResponse)
async def read_item(request: fastapi.Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/input")
async def get_item(request: fastapi.Request, username: str = fastapi.Form(...)):
    # return templates.TemplateResponse('index.html', {'request': request, 'name': username})
    print({'request': request, 'name': username})
    return {username}
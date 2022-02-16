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
import generate_map

app = fastapi.FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def something():
    response = RedirectResponse("/input")
    return response


@app.get('/input', response_class=HTMLResponse)
def read_item(request: fastapi.Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/input")
def get_item(request: fastapi.Request, username: str = fastapi.Form(...)):
    # return templates.TemplateResponse('index.html', {'request': request, 'name': username})
    print({'request': request, 'name': username})
    generate_map.main(username)
    response = RedirectResponse("/result")
    response.status_code = 302 # to avoid " '405 methond not allowed' response"
    return response


@app.get("/result", response_class=HTMLResponse)
def show_result(request: fastapi.Request):
    return templates.TemplateResponse('map.html', {"request": request})
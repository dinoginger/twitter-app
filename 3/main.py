"""
Lab 2-3
Marko Ruzak CS-1

Simple web application which uses TwitterAPI
and Leaflet.js to map given users' locations on map.

Main script.
"""
import fastapi
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import generate_map
from geopy.exc import GeocoderTimedOut

app = fastapi.FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def something():
    response = RedirectResponse("/input")
    return response


@app.get('/input', response_class=HTMLResponse)
def read_item(request: fastapi.Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/input")
async def get_item(request: fastapi.Request, username: str = fastapi.Form(...)):
    # return templates.TemplateResponse('index.html', {'request': request, 'name': username})
    print({'request': request, 'name': username})
    try:
        generate_map.main(username)
    except GeocoderTimedOut:
        return {"Geocode timeout:": " please try again later"}
    except Exception as e:
        return e.__repr__()
    response = RedirectResponse(f"/result?name={username}")
    response.status_code = 302  # to avoid " '405 method not allowed' response"
    return response


@app.get("/map.html", response_class=HTMLResponse)
async def show_result(request: fastapi.Request):
    return templates.TemplateResponse('map.html', {"request": request})


@app.get("/result", response_class=HTMLResponse)
async def show_result(request: fastapi.Request, name: str = "User", action: str = "Default"):
    if action == "Back":
        return RedirectResponse("/input")
    elif action == "Open in fullscreen":
        return RedirectResponse("/map.html")
    return templates.TemplateResponse('result.html', {"request": request, "name": name})

"""
Script which is responsible for generating map,
based on data recieved from TwitterAPI
"""
from locations import get_locations
import folium
from geopy.geocoders import Nominatim


def main(username: str):
    """
    Main script here.
    :param username: given on input username.
    :return: None
    """
    locator = Nominatim(user_agent="twitter-web-map")
    response, user_location = get_locations(username)
    followers = response["data"]
    coord = locator.geocode(user_location)

    try:
        usr_coord = (coord.latitude, coord.longitude)
        usr_addrs = get_percise_location(usr_coord, locator)
    except AttributeError:
        usr_coord = None
        usr_addrs = None
    for person in followers:
        if "location" not in person:
            continue
        person["coordinates"] = locator.geocode(person["location"])
        try:
            pl_lat = person["coordinates"].latitude
            pl_long = person["coordinates"].longitude
            person["coordinates"] = (pl_lat, pl_long)
            person["address"] = get_percise_location(person["coordinates"], locator)
            print(person["coordinates"], person["address"])
        except AttributeError:
            continue
    create_map(followers, username, usr_coord, usr_addrs)


def create_map(followers, username, user_coordinates, user_address):
    """
    For creating map.

    :param followers: dict (deserialized json from TwitterAPI)
    :param username: username given on input
    :param user_coordinates: coordinates recieved after first TwitterAPI call.
    :param user_address: retrieved by our additional function "get_percise_location()"
    :return: None. Generates and saves html map into "/templates" folder
    """
    mapp = folium.Map(zoom_start=15)
    locations = folium.FeatureGroup(name=f"{username}'s friends locations!")
    for person in followers:
        if "coordinates" not in person:
            continue
        if person["coordinates"] is None:
            continue
        name = person["name"]
        location = person["coordinates"]

        address = person["address"]

        popup = f'''<b>{person["name"]}</b><br>
        {address}'''
        locations.add_child(folium.Marker(name=name, location=location, popup=popup))
    mapp.add_child(locations)

    if user_coordinates is not None:
        address = user_address
        folium.CircleMarker(location=user_coordinates,
                            radius=5, popup=f'''<b>{username} is here!</b><br>
                                                    {address}''',
                            color='red', fill=True, fill_color='red').add_to(mapp)
    print("Created map.")
    mapp.save("templates/map.html")


def get_percise_location(coordinates, locator):
    """
    Additional function. Uses geopy to get city/county by coordinates.

    :param coordinates: tuple of floats. Latitude and longitude
    :param locator: geolocator obj,
    :return: string -> city/county
    """
    location = locator.reverse(coordinates)
    if "city" in location.raw["address"]:
        address = location.raw["address"]["city"]
    elif "county" in location.raw["address"]:
        address = location.raw["address"]["county"]
    else:
        address = "----"
    return address

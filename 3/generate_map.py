"""
Description later.
"""
from locations import  get_locations
import json
import folium
from geopy.geocoders import Nominatim


def main(username: str):
    locator = Nominatim(user_agent="twitter-web-map")
    response, user_location = get_locations(username)
    followers = response["data"]

    coord = locator.geocode(user_location)
    usr_coord = (coord.latitude, coord.longitude)

    for person in followers:
        person["coordinates"] = locator.geocode(person["location"])
        try:
            pl_lat = person["coordinates"].latitude
            pl_long = person["coordinates"].longitude
            person["coordinates"] = (pl_lat, pl_long)
        except AttributeError:
            continue
    create_map(followers, username, usr_coord)

def create_map(followers, username, user_coordinates):
    mapp = folium.Map(zoom_start=15)
    locator2 = Nominatim(user_agent="for-city")
    locations = folium.FeatureGroup(name=f"{username}'s friends locations!")
    # if type(user_coordinates) != str or type(user_coordinates) != None:
    #     folium.CircleMarker(location=user_coordinates,
    #                     radius=5, popup='I am here!',
    #                     color='red', fill=True, fill_color='red').add_to(mapp)
    for person in followers:
        if person["coordinates"] is None:
            continue
        name = person["name"]
        location = person["coordinates"]
        print(location)
        # --- GET CITY
        location2 = locator2.reverse(person["coordinates"])
        try:
            address = location2.raw["address"]["city"]
        except KeyError: # if no city:
            address = location2.raw["address"]["county"]
        # ---
        popup = f'''<b>{person["name"]}</b><br>
        {address}'''
        locations.add_child(folium.Marker(name=name, location=location, popup=popup))
    mapp.add_child(locations)
    print("Created map.")
    mapp.save("templates/map.html")


if __name__ == "__main__":
    main("gingerddd")

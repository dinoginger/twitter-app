"""
Script for retrieving TwitterAPI data.
"""
import hidden  # just a place with our twitter api keys.
import requests


def connect_to_endpoint(params, username):
    keys = hidden.oauth()
    bearer_oauth = {"Authorization": f"Bearer {keys['bearer']}"}

    # Get user data (location and ID)
    response_usr = requests.get(f"https://api.twitter.com/2/users/by/username/{username}",
                                headers=bearer_oauth, params={"user.fields": "location"})
    if response_usr.status_code != 200:
        raise Exception(response_usr.status_code, "Invalid username.")
    print(response_usr.json())
    id = response_usr.json()["data"]["id"]
    if "location" in response_usr.json()["data"]:
        location = response_usr.json()["data"]["location"]
    else:
        location = None
    # Get followers data.
    url = f"https://api.twitter.com/2/users/{id}/followers"
    response = requests.get(url, headers=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response_dict = response.json()
    return response_dict, location


def get_locations(username):
    search_params = {"max_results": 100, "user.fields": "id,location"}
    json_response, user_location = connect_to_endpoint(search_params, username)
    return json_response, user_location

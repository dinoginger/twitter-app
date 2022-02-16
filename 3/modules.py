"""
Add later
"""
import json
import hidden  # just a place with our twitter api keys.
import requests


def connect_to_endpoint(params, username):
    keys = hidden.oauth()
    bearer_oauth = {"Authorization": f"Bearer {keys['bearer']}"}
    response_usr = requests.get(f"https://api.twitter.com/2/users/by/username/{username}",
                                headers=bearer_oauth)
    id = response_usr.json()["data"]["id"]

    url = f"https://api.twitter.com/2/users/{id}/followers"
    response = requests.get(url, headers=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_locations(username):
    search_params = {"max_results": 3, "user.fields": "id,location"}
    json_response = connect_to_endpoint(search_params, username)
    print(json.dumps(json_response, indent=4, sort_keys=True))

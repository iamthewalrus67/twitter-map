'''
Module for working Twitter API.
'''

import os
import requests
import geo_helper


def get_user_friends(username, num_of_friends):
    base_url = 'https://api.twitter.com/'

    with open(os.path.join(os.path.dirname(__file__), 'bearer_token'), 'r') as token:
        bearer_token = token.read()

    search_url = f'{base_url}1.1/friends/list.json'

    search_headers = {
        'Authorization': f'Bearer {bearer_token}'
    }

    search_params = {
        'screen_name': f"@{username.replace('@', '')}",
        'count': num_of_friends
    }

    response = requests.get(
        search_url, headers=search_headers, params=search_params)

    json_response = response.json()
    return json_response['users']
    # pprint.pprint(json_response)

    # with open('obama.json', 'w') as f:
    #     json.dump(json_response, f)


def get_users_coordinates(users: list):
    unique_locations = []
    names_and_coordinates = []
    for user in users:
        if user['location'] not in unique_locations:
            names_and_coordinates.append(
                [user['screen_name'], geo_helper.get_coordinates(user['location'])])
            unique_locations.append(user['location'])

    return names_and_coordinates


if __name__ == '__main__':
    users = get_user_friends('donaldTrump', 10)
    print(get_users_coordinates(users))

"""
TwiterApiReader by Ustym Hanyk
"""
import requests
import json
from pprintpp import pprint as pp

def get_user_data(username):
    """
    Gets data about a specific twitter profile
    """
    base_url = "https://api.twitter.com/"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAFx4MwEAAAAA%2FZcsDE86L0w2He8EjBi1JbfDiMc%3DKysXA5FGeaV53qiLXXdmmXl62pa43vwhpFbpioTgromw6asmqZ"
    search_url = f"{base_url}1.1/users/show.json"
    search_headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    search_params = {
        "screen_name": f"{username}"
    }
    response = requests.get(search_url, headers=search_headers, params=search_params)

    json_response = response.json()
    # pp(json_response.keys())
    return response.json()

def start():
    """
    Starts the module
    """
    username = input("Enter a twitter username: @")
    username = "@" + username
    user_data = get_user_data(username)
    if len(user_data) == 1:  # if error
        print(user_data['errors'][0]["message"])
    print(f"What info do you want to know about {username} twitter profile?")

    # a list of available properties
    key_list = [info for info in user_data.keys() if isinstance(user_data[info], type(None)) == False]

    for num, key in enumerate(key_list):
        print(num, key, type(user_data[key]))
    key_name = int(input("Enter a number to navigate: "))

    if isinstance(user_data[key_list[key_name]], dict):
        print(f"Here is your '{key_list[key_name]}' dictionary:")
        return pp(user_data[key_list[key_name]])
    else:
        return print(user_data[key_list[key_name]])

if __name__ == '__main__':
    start()

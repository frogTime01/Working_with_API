import requests
from pprint import pprint


def get_group_names(access_token, user_id):
    url = f'https://api.vk.com/method/groups.get?user_id={user_id}&access_token={access_token}&v=5.131'
    response = requests.get(url)

    if response.status_code == 200:
        groups = response.json()
        pprint(groups)
    else:
        print('error')


TOKEN = "your token"
USER_ID = "your id"


get_group_names(TOKEN, USER_ID)

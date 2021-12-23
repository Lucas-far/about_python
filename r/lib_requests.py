

"""
Módulo >>> lib_requests.py

Objetivo:
         não sei exatamente.

Instalação:
           pip install requests
"""

from pprint import pprint
import requests

def get_github_user_avatar(username: str) -> str:
    """"""
    github = 'https://api.github.com/users/'
    url = f'{github}{username}'
    the_return = requests.get(url).json()
    # the_return2 = requests.get(url).json()['avatar_url']
    return the_return
    # return the_return2

if __name__ == '__main__':
    pprint(get_github_user_avatar('Lucas-far'))

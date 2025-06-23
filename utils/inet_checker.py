'''Internet checker utility'''

import requests

def check_inet():
    '''Check for internet connection'''

    try:
        requests.get("https://github.com", timeout=10)
    except requests.exceptions.RequestException as e:
        return e

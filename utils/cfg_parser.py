'''Config parser'''
import json
from colorama import Fore

def get_cfg_values() -> dict:
    '''Get config values'''
    try:
        with open('settings.json', "r+", encoding='utf-8') as cfg:
            cfg = json.load(cfg)
    except FileNotFoundError:
        exit("[-] Settings file doesn't exist!")
    except PermissionError:
        exit("[-] Settings file cannot be read due to permissions!")
    except IOError:
        exit("[-] Input/Output error while reading settings file")

    return cfg

def check_cfg_values(name: str, value: bool) -> dict:
    '''Check parameters for validity and return their values'''

    # We should check value type, because user could entered the wrong type
    if isinstance(value, bool) and value is True:
        return {name: True}
    else:
        return {name: False}

def parse_cfg() -> dict:
    '''Config parser and checker'''

    store_values = {}

    cfg = get_cfg_values()

    # First step - Try to get values
    try:
        cfg_params = {k: v for k, v in cfg.items()}
    except KeyError:
        exit("["+Fore.RED+"-"+Fore.RESET+"] Unable to parse some parameters from config")

    # Second step - Check values
    for k, v in cfg_params.items():
        store_values.update(check_cfg_values(k, v))

    return store_values

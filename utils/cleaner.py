'''Module for cleaning screen'''

import os

def clear():
    '''Clear function'''

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

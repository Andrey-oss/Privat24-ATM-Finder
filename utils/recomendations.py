import random
from colorama import Fore

recomend_list = ["Important! You only need to enter the city in Ukrainian language and keyboard layout, otherwise it won’t work!", "Interesting fact! If you enter any letters or numbers on the Ukrainian keyboard, the program will search for ATMs using the specified parameters"]

def recomend():
    '''Print recomendation'''

    print (f"[{Fore.YELLOW}+{Fore.RESET}] {random.choice(recomend_list)}")

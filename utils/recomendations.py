import random
from colorama import Fore

recomend_list = ["Важно! Город вводить нужно только руским языком и раскладкой, иначе не будет работать!", "Интересный факт! Если ввести на русской раскладке любые буквы или цифры, то программа будет искать банкоматы по указаным параметрам"]

def recomend():
    print ("["+Fore.YELLOW+"!"+Fore.RESET+"] "+random.choice(recomend_list))

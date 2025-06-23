'''The main part of app'''

try:
    from utils.logo import print_logo
    from utils.cleaner import clear
    from utils.recomendations import recomend
    from utils.inet_checker import check_inet
    from utils.cfg_parser import parse_cfg
    from utils.write_device_output import write_device_output as WDO
    from colorama import Fore
    import requests
except ImportError as e:
    exit(f"Error: {e}")

cfg = parse_cfg()

URL = 'https://api.privatbank.ua/p24api/infrastructure?json&atm&address=&city={0}'

check_inet()

try:
    motd = cfg['MOTD']
    recomendations = cfg['RECOMENDATIONS']
    output_in_file = cfg['OUTPUT_IN_FILE']
except KeyError:
    exit(f"[{Fore.RED}-{Fore.RESET}] Unable to parse some parameters from config")

cfg = parse_cfg()

if cfg['MOTD']:
    clear()
    print_logo()

if cfg['RECOMENDATIONS']:
    recomend()

city = input("City: ")

city_request = requests.get(URL.format(city), timeout=10)

if city_request.status_code == 502:
    print (f"[{Fore.RED}-{Fore.RESET}] Entered city is invalid")

elif city_request.status_code == 503:
    print (f"[{Fore.RED}-{Fore.RESET}] Server is busy, try later")

elif city_request.status_code == 504:
    print (f"[{Fore.RED}-{Fore.RESET}] Too many requests, try again")

else:
    city_dump = city_request.json()
    try:
        devices = city_dump['devices']
    except KeyError:
        exit("Unknown error occurred! Cannot to parse response")

    if cfg['OUTPUT_IN_FILE']:
        print(f"\n[{Fore.YELLOW}!{Fore.RESET}] Results will be written in results.txt")
        with open("results.txt", 'w', encoding='utf-8') as f:
            for i, device in enumerate(devices, 1):
                output = WDO(device, i)
                print(output)
                f.write(output + "\n\n")
    else:
        for i, device in enumerate(devices, 1):
            print(WDO(device, i))

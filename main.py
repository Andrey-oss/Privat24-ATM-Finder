try:
   from utils.logo import print_logo
   from utils.cleaner import clear
   from utils.recomendations import recomend
except Exception:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Ядро плагинов не установлено!")
   exit()
import json
import os
try:
   import requests
except Exception:
   print ("Модуль requests не установлен!")
   exit()
try:
   from colorama import Fore
except Exception:
   print ("Модуль colorama не установлен!")

file_output = "FALSE"
num_of_json = 0
num_of_atm = 1

# Reading config

try:
   requests.get("https://github.com", timeout=10)
except Exception:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Нету доступа к интернету!")
   exit()

try:
   jsonFile = open("settings.json", 'r')
   jsonObject = json.load(jsonFile)
   jsonFile.close()
except Exception:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Файл настроек не найден!")
   exit()

try:
   motd = jsonObject['MOTD']
except Exception:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Неверный формат файла настроек!")
   exit()

try:
   recomendations = jsonObject['RECOMENDATIONS']
except Exception:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Неверный формат файла настроек!")
   exit()

try:
   output_in_file = jsonObject['OUTPUT_IN_FILE']
except Exception:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Неверный формат файла настроек!")
   exit()

if motd == "TRUE":
   clear()
   print_logo()
elif motd == "FALSE":
   clear()
elif motd == "":
   clear()
   print_logo()
   print ("["+Fore.YELLOW+"!"+Fore.RESET+"] Настройки для параметра MOTD не заданы, по умолчанию будет TRUE")
   motd == "TRUE"
else:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Неверный формат файла настроек!")
   exit()

if recomendations == "TRUE":
   recomend()
   print ()
elif recomendations == "FALSE":
   print ()
elif recomendations == "":
   print ("["+Fore.YELLOW+"!"+Fore.RESET+"] Настройки для параметра RECOMENDATIONS не заданы, по умолчанию будет TRUE")
   recomendations == "TRUE"
else:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Неверный формат файла настроек!")
   exit()

if output_in_file == "TRUE":
   file_output = "TRUE"
elif output_in_file == "FALSE":
   file_output = "FALSE"
elif output_in_file == "":
   print ("["+Fore.YELLOW+"!"+Fore.RESET+"] Настройки для параметра OUTPUT_IN_FILE не заданы, по умолчанию будет FALSE")
   file_output = "FALSE"
else:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Неверный формат файла настроек!")
   exit()

# End of reading config

city = input("Город: ")

city_request = requests.get("https://api.privatbank.ua/p24api/infrastructure?json&atm&address=&city="+city)
if city_request.status_code == 502:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Произошла ошибка! Неверно введен город")

elif city_request.status_code == 503:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Сервер не отвечает! Повторите попытку позже")

elif city_request.status_code == 504:
   print ("["+Fore.RED+"-"+Fore.RESET+"] Слишком много запросов! Повторите попытку позже")

else:
   if file_output == "TRUE":
      city_dump = requests.get("https://api.privatbank.ua/p24api/infrastructure?json&atm&address=&city="+city).json()
      print ()
      y = json.dumps(city_dump)
      jsonDict = json.loads(y)
      cycle_num = len(jsonDict['devices'])
      f = open("results.txt", 'w')
      print ("["+Fore.YELLOW+"!"+Fore.RESET+"] Результат будет записан в файл results.txt по указанию аргумента TRUE в OUTPUT_IN_FILE")
      for i in range(cycle_num):
         print ()
         print ("{} Банкомат".format(num_of_atm))
         f.write("{} Банкомат".format(num_of_atm)+"\n")
         f.write(" \n")
         print ()
         y = json.dumps(city_dump)
         jsonDict = json.loads(y)
         devices = jsonDict['devices']
         y = json.dumps(devices)
         jsonDict = json.loads(y)
         dump = jsonDict[num_of_json]
         y = json.dumps(dump)
         jsonDict = json.loads(y)
         type = jsonDict['type']
         if type == "ATM":
            type = "ATM (банкомат)"
         else:
            type = type
         print ("Тип устройства: "+type) # Type checker
         f.write("Тип устройства: "+type+"\n")
         y = json.dumps(dump)
         jsonDict = json.loads(y)
         print ("Широта: "+jsonDict['latitude']) # Latitude checker
         f.write("Широта: "+jsonDict['latitude']+"\n")
         y = json.dumps(dump)
         jsonDict = json.loads(y)
         print ("Долгота: "+jsonDict['longitude']) # Longitude checker
         f.write("Долгота: "+jsonDict['longitude']+"\n")
         y = json.dumps(dump)
         jsonDict = json.loads(y)
         print ("Расположения: "+jsonDict['fullAddressRu']) # Location checker
         f.write("Расположения: "+jsonDict['fullAddressRu']+"\n")
         y = json.dumps(dump)
         jsonDict = json.loads(y)
         print ("Здания: "+jsonDict['placeRu']) # Place checker
         f.write("Здания: "+jsonDict['placeRu']+"\n")
         print ()
         num_of_json = num_of_json + 1
         num_of_atm = num_of_atm + 1
         f.write(" \n")

   elif file_output == "FALSE":
        city_dump = requests.get("https://api.privatbank.ua/p24api/infrastructure?json&atm&address=&city="+city).json()
        print ()
        y = json.dumps(city_dump)
        jsonDict = json.loads(y)
        cycle_num = len(jsonDict['devices'])
        for i in range(cycle_num):
           print ()
           print ("{} Банкомат".format(num_of_atm))
           print ()
           y = json.dumps(city_dump)
           jsonDict = json.loads(y)
           devices = jsonDict['devices']
           y = json.dumps(devices)
           jsonDict = json.loads(y)
           dump = jsonDict[num_of_json]
           y = json.dumps(dump)
           jsonDict = json.loads(y)
           type = jsonDict['type']
           if type == "ATM":
              type = "ATM (банкомат)"
           else:
              type = type
           print ("Тип устройства: "+type) # Type checker
           y = json.dumps(dump)
           jsonDict = json.loads(y)
           print ("Широта: "+jsonDict['latitude']) # Latitude checker
           y = json.dumps(dump)
           jsonDict = json.loads(y)
           print ("Долгота: "+jsonDict['longitude']) # Longitude checker
           y = json.dumps(dump)
           jsonDict = json.loads(y)
           print ("Расположения: "+jsonDict['fullAddressRu']) # Location checker
           y = json.dumps(dump)
           jsonDict = json.loads(y)
           print ("Здания: "+jsonDict['placeRu']) # Place checker
           print ()
           num_of_json = num_of_json + 1
           num_of_atm = num_of_atm + 1


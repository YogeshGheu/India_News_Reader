import json
import requests
from time import sleep

def speaker(text):
       from win32com.client import Dispatch
       speak = Dispatch("SAPI.SpVoice")
       speak.Speak(text)

try: #for creating data.txt filr if dosen't exists. this will contain all the top 10 news of the day.
       with open("data.txt", "x") as createfile:
              createfile.close()
              pass
except FileExistsError:
       pass
with open("data.txt", "w") as erase: #to erase the file if you start the program again/ or on next day
       erase.write("")
       erase.close()

url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=29d4f69e0b7e44eaa01d62e6b6545394') #You can change the country as per your requirements
response = requests.get(url)
text = response.text
jsn = json.loads(text)
for i in range(0, 10):
       speaker(jsn['articles'][i]['title'])
       with open("data.txt", "a") as f:
              f.write(jsn['articles'][i]['title'])
              f.write("\n")
              sleep(1.5)
f.close()
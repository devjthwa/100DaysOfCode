import requests
import win32com.client as wincom
import json
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak("Hello! Welcome to the Weather Api Service, Please enter the city name in terminal")
city = input("Enter city : \n")
speak.Speak(city)
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r = requests.get(url)
# print(r.text)
weatherDic = json.loads(r.text)
w = weatherDic["current"]["temp_c"]
print(f"the current temperature in {city} is {w} degress")
speak.Speak(f"the current temperature in {city} is {w} degrees")
      
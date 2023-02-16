import requests
from bs4 import BeautifulSoup

def get_weather(city):

    weather = requests.get(f"https://sinoptik.ua/погода-{city}")
    soup = BeautifulSoup(weather.content)
    temp = soup.find("p",class_="today-temp").text

    return temp
# def get_holat(city):

#     weather = requests.get(f"https://sinoptik.ua/погода-{city}")
#     soup = BeautifulSoup(weather.content)
#     holat = soup.find("td",class_="p4 bR ")

#     return holat
# print(get_holat("фергана"))
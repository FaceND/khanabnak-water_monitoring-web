from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import os

load_dotenv()

stations_url = {
    "Klong_Bangdee":"https://khanabnak.ssru-watermonitoring.com/station_detail.php?p=MTI0MzU3MC45Mw==&ss=MTc3NjUyLjk5&s=MTU5ODg3Ni45MQ==",
    "Klong_Mabok":"https://khanabnak.ssru-watermonitoring.com/station_detail.php?p=MTI0MzU3MC45Mw==&ss=MTc3NjUyLjk5&s=MTQyMTIyMy45Mg==",
    "Wat_Bang_Udom":"https://khanabnak.ssru-watermonitoring.com/station_detail.php?p=MTI0MzU3MC45Mw==&ss=MTc3NjUyLjk5&s=MTA2NTkxNy45NA==",
    "Moo_2_Khanabnak":"https://khanabnak.ssru-watermonitoring.com/station_detail.php?p=MTI0MzU3MC45Mw==&ss=MTc3NjUyLjk5&s=MTI0MzU3MC45Mw=="
    }

stations_list_TH = {
        "Klong_Bangdee": "คลองบางดี",
        "Klong_Mabok": "คลองมาบออก",
        "Wat_Bang_Udom": "วัดบางอุดม",
        "Moo_2_Khanabnak": "หมู่บ้านเศรษฐกิจพอเพียงป่าขลู (หมู่ที่2)",
      }

def get_station_data(station_name):
    station_data = {'title':None,'temp':0, 'salinity':0, 'electcon':0, 'oxygen':0, 'BOD':0}
    if station_name in stations_url.keys():
        req = requests.get(stations_url[station_name])
        if req.status_code == 200:
            req.encoding = 'utf-8'
            soup = BeautifulSoup(req.text, 'html.parser')
            cards_data = soup.find_all('div',{'class':os.getenv("CLASS_ELEMENT")})
            for key, data in zip(list(station_data.keys())[1:], cards_data):
                station_data[key] = data.get_text().split(' ').pop(0)
        station_data['title'] = stations_list_TH[station_name]
    return station_data
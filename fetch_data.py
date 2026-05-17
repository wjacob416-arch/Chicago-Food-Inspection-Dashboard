import requests
import json
import database

api_url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json?$limit=1000"


def fetch_url():
    response = requests.get(api_url)
    data = response.json()
    return data

def load_data():
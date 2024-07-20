import requests
import json
import yaml
import time

BASE_URL = "https://astrosphericpublicaccess.azurewebsites.net/api"
URL_FORECAST = "GetForecastData_V1"
URL_SKY = "GetSky_V1"


def fetch_api_key() -> str:
    with open("../auth/api_key.yaml", 'r') as f:
        api_key = yaml.safe_load(f)["API_KEY"]
        return api_key


def fetch_forecast(latitude: float, longitude: float) -> dict:
    api_url = BASE_URL + '/' + URL_FORECAST
    api_data = {
        "Latitude": latitude,
        "Longitude": longitude,
        "APIKey": fetch_api_key(),
    }

    # Convert data to JSON format
    json_data_string = json.dumps(api_data)

    # Send POST request
    headers = {"Content-type": "application/json"}
    response = requests.post(api_url, data=json_data_string, headers=headers)

    # Handle response from API
    if response.status_code == 200:
        astro_data = json.loads(response.text)
        return astro_data
    else:
        return {}


def fetch_sky(latitude: float, longitude: float, ms_since_epoc: int) -> dict:
    api_url = BASE_URL + '/' + URL_SKY
    api_data = {
        "Latitude": latitude,
        "Longitude": longitude,
        "MSSinceEpoch": ms_since_epoc,
        "APIKey": fetch_api_key(),
    }

    # Convert data to JSON format
    json_data_string = json.dumps(api_data)

    # Send POST request
    headers = {"Content-type": "application/json"}
    response = requests.post(api_url, data=json_data_string, headers=headers)

    # Handle response from API
    if response.status_code == 200:

        astro_data = json.loads(response.text)
        # astro_data = response.text
        return astro_data
    else:
        return {}
    pass


LATITUDE = 30.218910
LONGITUDE = -97.854607
MS_SINCE_EPOCH = int(time.time() * 1000)

forecast = fetch_forecast(LATITUDE, LONGITUDE)
print(forecast)
print()

sky = fetch_sky(LATITUDE, LONGITUDE, MS_SINCE_EPOCH)
print(sky)
print()

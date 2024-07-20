import requests
import json
from datetime import datetime

BASE_URL = "https://astrosphericpublicaccess.azurewebsites.net/api"
URL_FORECAST = "GetForecastData_V1"
URL_SKY = "GetSky_V1"
API_KEY = "21505ACC6108BA40CFB312CE011FBDB1B91278D514FF8D81E198E80985EB2D1F3E8FC234"
LATITUDE = 30.218910
LONGITUDE = -97.854607


def fetch_astro_data():

    API_URL = BASE_URL + '/' + URL_FORECAST

    # Data to send in the request
    api_data = {
        "Latitude": LATITUDE,
        "Longitude": LONGITUDE,
        "APIKey": API_KEY
    }

    # Convert data to JSON format
    json_data_string = json.dumps(api_data)

    # Send POST request
    headers = {"Content-type": "application/json"}
    response = requests.post(API_URL, data=json_data_string, headers=headers)

    # Handle response from API
    if response.status_code == 200:
        astro_data = json.loads(response.text)

        return astro_data
    else:
        print(f"Error fetching forecast. Status code: {response.status_code}")


if __name__ == "__main__":
    # Calling the function to fetch the forecast
    forecast_data = fetch_astro_data()
    print(forecast_data)
    pass

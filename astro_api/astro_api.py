import os
import json
import time
import requests
from enum import Enum
from typing import Union
from dotenv import load_dotenv


class AstroDtype(Enum):
    FORECAST = "GetForecastData_V1"
    SKY_MAP = "GetSky_V1"


def fetch_astro_data(dtype: Union[AstroDtype | str], loc_coords: tuple, ms_since_epoch=None) -> dict:
    if type(dtype) is str:
        dtype = AstroDtype[dtype.upper()]
    if ms_since_epoch is None:
        ms_since_epoch = round(time.time() * 1000)

    # Build the API URL
    base_url = "https://astrosphericpublicaccess.azurewebsites.net/api"
    api_url = base_url + "/" + str(dtype.value)

    # Parse the user inputs
    api_data = {
        "Latitude": loc_coords[0],
        "Longitude": loc_coords[1],
        "APIKey": os.getenv('API_KEY'),
    }
    if dtype == AstroDtype.SKY_MAP:
        api_data["MSSinceEpoch"] = ms_since_epoch

    # Convert data to JSON format
    json_data_string = json.dumps(api_data)

    # Send POST request
    headers = {"Content-type": "application/json"}
    response = requests.post(api_url, data=json_data_string, headers=headers)

    # Handle response from API
    if response.status_code == 200:
        response_text = response.text
        if response_text.startswith('\ufeff'):
            response_text = response.text[1:]
        astro_data = json.loads(response_text)
        return astro_data
    else:
        print(response.content.decode('utf-8'))
        return {}


if __name__ == "__main__":
    load_dotenv()
    LATITUDE = 30.218910
    LONGITUDE = -97.854607
    forecast_data = fetch_astro_data(dtype=AstroDtype.FORECAST, loc_coords=(LATITUDE, LONGITUDE))
    skymap_data = fetch_astro_data(dtype=AstroDtype.SKY_MAP, loc_coords=(LATITUDE, LONGITUDE))
    pass

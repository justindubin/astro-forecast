import requests
import json
import yaml
import time
from enum import Enum
from typing import Union


class AstroDtype(Enum):
    FORECAST = "GetForecastData_V1"
    SKY_MAP = "GetSky_V1"


def fetch_api_key() -> str:
    with open("../auth/api_key.yaml", 'r') as f:
        api_key = yaml.safe_load(f)["API_KEY"]
        return api_key


def fetch_astro_data(dtype: Union[AstroDtype | str], loc_coords: tuple, ms_since_epoch=None) -> dict:
    if type(dtype) is str:
        dtype = AstroDtype[dtype.upper()]
    if ms_since_epoch is None:
        ms_since_epoch = round(time.time() * 1000)

    # Build the API URL and construct the parameter container
    base_url = "https://astrosphericpublicaccess.azurewebsites.net/api"
    api_url = base_url + "/" + str(dtype.value)
    latitude, longitude = loc_coords[0], loc_coords[1]
    api_data = {
        "Latitude": latitude,
        "Longitude": longitude,
        "APIKey": fetch_api_key(),
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
        if response.text.startswith('\ufeff'):
            response_text = response.text[1:]
        astro_data = json.loads(response_text)
        return astro_data
    else:
        print(response.content.decode('utf-8'))
        return {}


if __name__ == "__main__":
    LATITUDE = 30.218910
    LONGITUDE = -97.854607
    MS_SINCE_EPOCH = int(time.time() * 1000)
    data = fetch_astro_data(dtype=AstroDtype.SKY_MAP, loc_coords=(LATITUDE, LONGITUDE))

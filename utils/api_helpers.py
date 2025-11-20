import requests
from config.settings import BASE_URL

def get_candlestick_data(instrument_name, timeframe, context=None):
    url = f"{BASE_URL}/public/get-candlestick"

    params = {
        "instrument_name": instrument_name,
        "timeframe": timeframe
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    if context is not None:
        context.request_url = response.request.url
        context.api_response = response.json()

    return response.json()
import requests
from django.conf import settings

def fetch_latest_prices(ticker):
    url =  f"http://api.marketstack.com/v1/eod"

    params = {"access_key": settings.API_KEY,
              "symbols":ticker,
                }

    r = requests.get(url, params=params)
    data = r.json()
    
    print(f"URL called: {r.url}")  

    print(r.status_code)
    print(r.text)
    if not data.get("data"):
        return None

    result = data["data"][0]

    print(data)
    return {
        "open": result["open"],
        "high": result["high"],
        "low": result["low"],
        "close": result["close"],
        "volume": result["volume"],
        "timestamp": result["date"], 
    }



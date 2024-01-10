import requests
import requests_cache
from datetime import timedelta

standings_base_url = 'https://api-web.nhle.com/v1/standings/'

requests_cache.install_cache(
    'data/rinkrat_cache', # todo - find root and place in data folder
    'sqlite',
    expire_after = timedelta(0, 0, 0, 0, 5.0, 0, 0)
)

def _get(url: str, params=None, **kwargs) -> dict:
    try:
        response = requests.get(url, params=params, **kwargs)
        response.raise_for_status()

        try:
            result = response.json()
            return result
        except requests.exceptions.JSONDecodeError as e:
            raise SystemExit(e)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
def request_league_standings(date: str, params=None, **kwargs) -> dict:
    """
    Sends a GET request for the league standings on specified date (optional).
    Returns the json-encoded content of a response, if any.
    """

    url = '{}{}'.format(standings_base_url, date)

    return _get(url, params=params, **kwargs)

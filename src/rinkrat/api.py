import requests
import requests_cache
from datetime import timedelta

requests_cache.install_cache(
    'data/rinkrat_cache',
    'sqlite',
    expire_after = timedelta(0, 0, 0, 0, 5.0, 0, 0)
)

def get(url: str, params=None, **kwargs) -> dict:
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

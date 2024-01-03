import requests
import requests_cache
from datetime import timedelta

standings_url = 'https://api-web.nhle.com/v1/standings/now'

urls_expire_after = {
    standings_url: timedelta(0, 0, 0, 0, 5, 0, 0) # 5 minutes
}

requests_cache.install_cache(
    '../data/rinkrat_cache',
    'sqlite',
    urls_expire_after = urls_expire_after,
)

def get_current_standings() -> dict:
    try:
        response = requests.get(standings_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

import requests

'''
    break down the data returned from the api
'''

standings_url = 'https://api-web.nhle.com/v1/standings/now'

def main() -> None:
    try:
        response = requests.get(standings_url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    print(f'response type: {type(response.json())}')

    standings = response.json()['standings']

    print(f'standings type: {type(standings)}')

    for team in standings:
        print(f'team type: {type(team)}\n')

        for key, value in team.items():
            print(f'{key: <25}: {value}')

        # print for just one team
        break

if __name__ == '__main__':
    main()

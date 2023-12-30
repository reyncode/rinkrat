'''
    File: rinkrat.py
    Author: Alex Reynolds

    Description: a tool for querying nhl team stats.
'''

import requests
import requests_cache
from datetime import timedelta
from typing import List

standings_url = 'https://api-web.nhle.com/v1/standings/now'

urls_expire_after = {
    standings_url: timedelta(0, 0, 0, 0, 5, 0, 0) # 5 minutes
}

requests_cache.install_cache(
    'group_parsing_cache',
    'sqlite',
    urls_expire_after = urls_expire_after,
)

def parse_league(standings: List) -> dict:
    league = []

    for team in standings:
        league.append(team)

    result = dict()
    result['league'] = league

    return result

def parse_conference(standings: List) -> dict:
    eastern = []
    western = []

    for team in standings:
        
        if team['conferenceName'] == 'Eastern':
            eastern.append(team)

        elif team['conferenceName'] == 'Western':
            western.append(team)

    result = dict()
    result['eastern'] = eastern
    result['western'] = western

    return result

def parse_division(standings: List) -> dict:
    atlantic = []
    metropolitan = []
    central = []
    pacific = []

    for team in standings:

        if team['divisionName'] == 'Atlantic':
            atlantic.append(team)

        elif team['divisionName'] == 'Metropolitan':
            metropolitan.append(team)

        elif team['divisionName'] == 'Central':
            central.append(team)

        elif team['divisionName'] == 'Pacific':
            pacific.append(team)

    result = dict()
    result['atlantic'] = atlantic
    result['metropolitan'] = metropolitan
    result['central'] = central
    result['pacific'] = pacific

    return result

def parse_wild_card(standings: List) -> dict:
    atlantic = []
    metropolitan = []
    central = []
    pacific = []
    wild_card_east = []
    wild_card_west = []

    for team in standings:

        if team['divisionName'] == 'Atlantic' and team['wildcardSequence'] == 0:
            atlantic.append(team)

        elif team['divisionName'] == 'Metropolitan' and team['wildcardSequence'] == 0:
            metropolitan.append(team)
        
        elif team['divisionName'] == 'Central' and team['wildcardSequence'] == 0:
            central.append(team)
        
        elif team['divisionName'] == 'Pacific' and team['wildcardSequence'] == 0:
            pacific.append(team)
        
        elif team['conferenceName'] == 'Eastern':
            wild_card_east.append(team)
        
        elif team['conferenceName'] == 'Western':
            wild_card_west.append(team)

    result = dict()

    result['atlantic'] = atlantic
    result['metropolitan'] = metropolitan
    result['wild_card_east'] = wild_card_east
    result['central'] = central
    result['pacific'] = pacific
    result['wild_card_west'] = wild_card_west

    return result

def main() -> None:

    try:
        response = requests.get(standings_url)

        # groups the teams by the specified grouping
        # result = parse_league(response.json()['standings'])
        # result = parse_conference(response.json()['standings'])
        # result = parse_division(response.json()['standings'])
        result = parse_wild_card(response.json()['standings'])

        for group in result:

            # group header
            caps = [word.capitalize() for word in group.replace("_", " ").split(" ")]
            print(' '.join(caps))

            print(f'{"Team": <26}{"GP": <4}{"W": <4}{"L": <4}{"OTL": <4}{"PTS": <4}')

            # ranked team stats
            for team in result[group]:

                print('{0[teamName][default]:<26}{0[gamesPlayed]:<4}{0[wins]:<4}'
                      '{0[losses]:<4}{0[otLosses]:<4}{0[points]:<4}'.format(team))

            print()

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

if __name__ == '__main__':
    main()

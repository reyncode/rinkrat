import argparse
from datetime import datetime

import api
import order

def display(result: dict) -> None:
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

def get_standings(args) -> None:

    date = datetime.now()

    now = '{:04d}-{:02d}-{:02d}'.format(date.year, date.month, date.day)

    response = api.request_league_standings(now)

    teams = response['standings']
    result = dict()

    if args.overall:
        result = order.order_by_overall(teams)

    if args.conference:
        result = order.order_by_conference(teams)

    if args.division:
        result = order.order_by_division(teams)

    if args.wild_card:
        result = order.order_by_wild_card(teams)

    display(result)

def _parse_args():
    parser = argparse.ArgumentParser(prog = 'rinkrat')

    parser.set_defaults(func = lambda x: None)

    subparsers = parser.add_subparsers()

    standings_parser = subparsers.add_parser('standings')

    standings_group = standings_parser.add_mutually_exclusive_group()

    # accept nothing or a string date (0 or 1 args)
    standings_group.add_argument('-o', '--overall', action = 'store_true')

    standings_group.add_argument('-c', '--conference', action = 'store_true')
    standings_group.add_argument('-d', '--division', action = 'store_true')
    standings_group.add_argument('-w', '--wild-card', action = 'store_true')

    standings_parser.set_defaults(func = get_standings)

    return parser.parse_args()

def main() -> None:
    args = _parse_args()

    args.func(args)

if __name__ == '__main__':
    main()

import argparse
from datetime import datetime

import api
import order

result = dict()

todays_date = datetime.now()
today_string = '{:04d}-{:02d}-{:02d}'.format(todays_date.year, todays_date.month, todays_date.day)

def display_standings(result: dict, date) -> None:

    print(f'{"Date": <26}{date}')

    for group in result:

        # group header
        caps = [word.capitalize() for word in group.replace("_", " ").split(" ")]
        print(f'{" ".join(caps)}')

        print(f'{"Team": <26}{"GP": <4}{"W": <4}{"L": <4}{"OTL": <4}{"PTS": <4}')

        # ranked team stats
        for team in result[group]:

            print('{0[teamName][default]:<26}{0[gamesPlayed]:<4}{0[wins]:<4}'
                  '{0[losses]:<4}{0[otLosses]:<4}{0[points]:<4}'.format(team))

        print()

def overall(teams, date):
    result = order.order_by_overall(teams)
    display_standings(result, date)

def conference(teams, date):
    result = order.order_by_conference(teams)
    display_standings(result, date)

def division(teams, date):
    result = order.order_by_division(teams)
    display_standings(result, date)

def wild_card(teams, date):
    result = order.order_by_wild_card(teams)
    display_standings(result, date)

def validate_date(text: str) -> datetime:
    for fmt in ('%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d', '%Y%m%d'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise SystemExit(ValueError('Invalid date format: please use YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD or YYYYMMDD'))

class StandingsAction(argparse.Action):
    def __init__(self, option_strings, order,
                 *args, **kwargs):
        self._order = order
        super(StandingsAction, self).__init__(option_strings=option_strings,
                                              *args, **kwargs)

    def __call__(self, parser, args, values, option_string=None):
        setattr(args, self.dest, values)

        query_date = validate_date(values)
        query_date_string = '{:04d}-{:02d}-{:02d}'.format(query_date.year, 
                                                          query_date.month, 
                                                          query_date.day)

        response = api.request_league_standings(query_date_string)

        self._order(response['standings'], values)

def _parse_args():
    parser = argparse.ArgumentParser(prog = 'rinkrat')

    subparsers = parser.add_subparsers()

    standings_parser = subparsers.add_parser('standings')

    standings_group = standings_parser.add_mutually_exclusive_group()

    standings_group.add_argument('-o', '--overall', nargs='?', const=today_string,
                                 action=StandingsAction, order=overall,
                                 metavar='YYYY-MM-DD')

    standings_group.add_argument('-c', '--conference', nargs='?', const=today_string,
                                 action=StandingsAction, order=conference)

    standings_group.add_argument('-d', '--division', nargs='?', const=today_string,
                                 action=StandingsAction, order=division)

    standings_group.add_argument('-w', '--wild-card', nargs='?', const=today_string,
                                 action=StandingsAction, order=wild_card)

    return parser.parse_args()

def main() -> None:
    args = _parse_args()

if __name__ == '__main__':
    main()

import argparse
from datetime import datetime
from typing import List

import api

standings_base_url = 'https://api-web.nhle.com/v1/standings/'

class Standings:
    def __init__(self, argv: List[str]) -> None:
        # use today's date as the default
        today = datetime.now()
        self.date = "{:04d}-{:02d}-{:02d}".format(
            today.year, 
            today.month, 
            today.day
        )

        parser = argparse.ArgumentParser(prog="standings")
        group = parser.add_mutually_exclusive_group()

        # define the standings options

        group.add_argument(
            "-o",
            "--overall",
            action="store_true",
            dest="overall",
            help="results ranked by league standing"
        )

        group.add_argument(
            "-c",
            "--conference",
            action="store_true",
            dest="conference",
            help="results ranked by conference standing"
        )

        group.add_argument(
            "-d",
            "--division",
            action="store_true",
            dest="division",
            help="results ranked by division standing"
        )

        group.add_argument(
            "-w",
            "--wild-card",
            action="store_true",
            dest="wild_card",
            help="results ranked by wild card standing"
        )

        parser.add_argument(
            "date",
            nargs="?",
            default=self.date,
            help="query rankings for this date, YYYY-MM-DD",
        )
        
        # create a dictionary of options that contain values
        opts = vars(parser.parse_args(argv))
        self.opts = {k: v for k, v in opts.items() if v not in (None, "", False)}
        
        self.get_data()
        self.order_data()
        self.display()


    def get_data(self):
        date = validate_query_date(self.opts["date"])
        date_string = "{:04d}-{:02d}-{:02d}".format(
            date.year, 
            date.month, 
            date.day
        )

        url = '{}{}'.format(standings_base_url, date_string)

        # store the response data in our opts dict
        self.opts.setdefault("data", api.get(url))

    def order_data(self):
        if "overall" in self.opts:
            # TODO: refactor - this is duplicating data in a slightly different order
            self.opts.setdefault(
                "ranked", 
                order_by_overall(self.opts["data"]["standings"])
            )

        if "conference" in self.opts:
            # TODO: refactor - this is duplicating data in a slightly different order
            self.opts.setdefault(
                "ranked", 
                order_by_conference(self.opts["data"]["standings"])
            )

        if "division" in self.opts:
            # TODO: refactor - this is duplicating data in a slightly different order
            self.opts.setdefault(
                "ranked", 
                order_by_division(self.opts["data"]["standings"])
            )

        if "wild_card" in self.opts:
            # TODO: refactor - this is duplicating data in a slightly different order
            self.opts.setdefault(
                "ranked", 
                order_by_wild_card(self.opts["data"]["standings"])
            )

    def display(self):
        print(f'{"Date": <26}{self.opts["date"]}')

        for group in self.opts["ranked"]:

            # group header
            caps = [word.capitalize() for word in group.replace("_", " ").split(" ")]
            print(f'{" ".join(caps)}')

            print(f'{"Team": <26}{"GP": <4}{"W": <4}{"L": <4}{"OTL": <4}{"PTS": <4}')

            # ranked team stats
            for team in self.opts["ranked"][group]:

                print('{0[teamName][default]:<26}{0[gamesPlayed]:<4}{0[wins]:<4}'
                      '{0[losses]:<4}{0[otLosses]:<4}{0[points]:<4}'.format(team))

            print()

def validate_query_date(text: str) -> datetime:
    for format in ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y%m%d"):
        try:
            return datetime.strptime(text, format)
        except ValueError:
            pass
        
    raise SystemExit(
        argparse.ArgumentError(
            argument=None,
            message="Invalid date supplied as an argument."
        )
    )

def order_by_overall(teams: List) -> dict:
    overall = []

    for team in teams:
        overall.append(team)

    result = dict()
    result['league'] = overall

    return result

def order_by_conference(teams: List) -> dict:
    eastern = []
    western = []

    for team in teams:
        
        if team['conferenceName'] == 'Eastern':
            eastern.append(team)

        elif team['conferenceName'] == 'Western':
            western.append(team)

    result = dict()
    result['eastern'] = eastern
    result['western'] = western

    return result

def order_by_division(teams: List) -> dict:
    atlantic = []
    metropolitan = []
    central = []
    pacific = []

    for team in teams:

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

def order_by_wild_card(teams: List) -> dict:
    atlantic = []
    metropolitan = []
    central = []
    pacific = []
    wild_card_east = []
    wild_card_west = []

    for team in teams:

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

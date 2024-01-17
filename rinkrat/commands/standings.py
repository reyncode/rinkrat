import argparse
from datetime import datetime
from typing import List

import api

standings_base_url = 'https://api-web.nhle.com/v1/standings/'

usage_str = """standings <command> [<args>]

commands:
  overall     results ranked by league standing
  conference  results ranked by conference standing
  division    results ranked by division standing
  wild        results ranked by wild card standing
"""

class Standings:
    def __init__(self, argv: List[str]) -> None:
        # use today's date as the default
        today = datetime.now()
        self.date = "{:04d}-{:02d}-{:02d}".format(
            today.year, 
            today.month, 
            today.day
        )

        parser = argparse.ArgumentParser(usage=usage_str)

        self.parser = parser

        parser.add_argument("ranking")
        
        parser.add_argument(
            "-d",
            "--date",
            nargs="?",
            default=self.date,
            metavar="YYYY-MM-DD",
            help="query rankings for this date, YYYY-MM-DD",
        )

        args = parser.parse_known_args(argv)

        # create a dictionary of options that contain values
        self.opts = {k: v for k, v in vars(args[0]).items() if v not in (None, "")}

        try:
            getattr(self, args[0].ranking)(args[1])
        except AttributeError:
            print(f"\"{args[0].ranking}\" is not a valid ranking", end="\n\n")
            parser.print_help()

        self.get_data()

        self.rank_results()

        self.display()

    def get_data(self):
        date = validate_query_date(self.opts["date"], self.parser)
        date_string = "{:04d}-{:02d}-{:02d}".format(
            date.year, 
            date.month, 
            date.day
        )

        url = '{}{}'.format(standings_base_url, date_string)

        self.opts.setdefault("data", api.get(url))

    def display(self):
        """Show the ranked results on the console"""

        """
        [date]

        [group-header]
        [team-stat-header]
        [ranked-team-stats]
        """

        # show the date
        print(f'{"Date": <26}{self.opts["date"]}', end="\n\n")

        for group, teams in self.opts["ranked"].items():
            # group header
            print(f"{group}")

            # team stat header
            print(f'{"Team": <26}{"GP": <4}{"W": <4}{"L": <4}{"OTL": <4}{"PTS": <4}')

            # ranked team stats
            for team in teams:
                print('{0[teamName][default]:<26}{0[gamesPlayed]:<4}{0[wins]:<4}'
                      '{0[losses]:<4}{0[otLosses]:<4}{0[points]:<4}'.format(team))

            print()

    def overall(self, argv):
        if argv:
            argparse.ArgumentParser.error(
                self=self.parser,
                message="overall does have a selection, see standings --help")
        else:
            self.opts.setdefault("selection", ["overall"])
        
    def conference(self, argv: List[str]):
        conferences = ["eastern", "western"]
        if any(i not in conferences for i in argv):
            argparse.ArgumentParser.error(
                self=self.parser,
                message="you can only use 'eastern' or 'western', see standings --help")
        else:
            selection = []
            if not argv:
                selection = ["eastern", "western"]
            else:
                [selection.append(x) for x in argv if x not in selection]

            self.opts.setdefault("selection", selection)
        
    def division(self, argv):
        divisions = ["atlantic", "metropolitan", "central", "pacific"]
        if any(i not in divisions for i in argv):
            argparse.ArgumentParser.error(
                self=self.parser,
                message="you can only use 'atlantic', 'metropolitan', 'central', 'pacific', see standings --help")
        else:
            selection = []
            if not argv:
                selection = ["atlantic", "metropolitan", "central", "pacific"]
            else:
                [selection.append(x) for x in argv if x not in selection]

            self.opts.setdefault("selection", selection)
        
    def wild(self, argv):
        conferences = ["eastern", "western"]
        if any(i not in conferences for i in argv):
            argparse.ArgumentParser.error(
                self=self.parser,
                message="you can only use 'eastern' or 'western', see standings --help")
        else:
            selection = []
            if not argv:
                selection = ["eastern", "western"]
            else:
                [selection.append(x) for x in argv if x not in selection]

            self.opts.setdefault("selection", selection)

    def rank_results(self):
        if self.opts["ranking"] == "overall":
            self.opts.setdefault(
                "ranked",
                ranked_by_overall(self, 
                                  self.opts["data"]["standings"]))

        if self.opts["ranking"] == "conference":
            self.opts.setdefault(
                "ranked",
                ranked_by_conference(self, 
                                     self.opts["data"]["standings"]))

        if self.opts["ranking"] == "division":
            self.opts.setdefault(
                "ranked",
                ranked_by_division(self, 
                                   self.opts["data"]["standings"]))

        if self.opts["ranking"] == "wild":
            self.opts.setdefault(
                "ranked",
                ranked_by_wild(self, 
                               self.opts["data"]["standings"]))

def ranked_by_overall(self, teams: List) -> dict:
    result = dict()
    name = str()

    for x in self.opts["selection"]:
        name = x.capitalize()
        result.setdefault(name, [])

    for team in teams:
        result[name].append(team)

    return result

def ranked_by_conference(self, teams: List) -> dict:
    result = dict()

    for x in self.opts["selection"]:
        result.setdefault(x.capitalize(), [])

    for team in teams:
        if team["conferenceName"] in result:
            result[team["conferenceName"]].append(team)

    return result

def ranked_by_division(self, teams: List) -> dict:
    result = dict()

    for x in self.opts["selection"]:
        result.setdefault(x.capitalize(), [])

    for team in teams:
        if team["divisionName"] in result:
            result[team["divisionName"]].append(team)

    return result

def ranked_by_wild(self, teams: List) -> dict:
    result = dict()

    for x in self.opts["selection"]:
        result.setdefault(x.capitalize(), [])

    for team in teams:
        if team["conferenceName"] in result:
            if team["wildcardSequence"] > 0:
                result[team["conferenceName"]].append(team)

    return result

def validate_query_date(text: str, parser: argparse.ArgumentParser) -> datetime:
    for format in ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y%m%d"):
        try:
            return datetime.strptime(text, format)
        except ValueError:
            pass
        
    argparse.ArgumentParser.error(
        self=parser, 
        message="invalid date format - use YYYY-MM-DD. see standings --help")


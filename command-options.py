import argparse

conferences = ['east', 'west']
divisions = ['atlantic', 'metropolitan', 'central', 'pacific']
teams = {
    'ANA': 'Anaheim Ducks',
    'ARI': 'Arizona Coyotes',
    'BOS': 'Boston Bruins',
    'BUF': 'Buffalo Sabres',
    'CAR': 'Carolina Hurricanes',
    'CBJ': 'Columbus Blue Jackets',
    'CGY': 'Calgary Flames',
    'CHI': 'Chicago Blackhawks',
    'COL': 'Colorado Avalanche',
    'DAL': 'Dallas Stars',
    'DET': 'Detroit Red Wings',
    'EDM': 'Edmonton Oilers',
    'FLA': 'Florida Panthers',
    'LAK': 'Los Angeles Kings',
    'MIN': 'Minnesota Wild',
    'MTL': 'Montréal Canadiens',
    'NJD': 'New Jersey Devils',
    'NSH': 'Nashville Predators',
    'NYI': 'New York Islanders',
    'NYR': 'New York Rangers',
    'OTT': 'Ottawa Senators',
    'PHI': 'Philadelphia Flyers',
    'PIT': 'Pittsburgh Penguins',
    'SEA': 'Seattle Kraken',
    'SJS': 'San Jose Sharks',
    'STL': 'St. Louis Blues',
    'TBL': 'Tampa Bay Lightning',
    'TOR': 'Toronto Maple Leafs',
    'VAN': 'Vancouver Canucks',
    'VGK': 'Vegas Golden Knights',
    'WPG': 'Winnipeg Jets',
    'WSH': 'Washington Capitals',
}

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage = '\n rinkrat [options]'
    )

    parser.add_argument(
        '-v', '--version',
        action = 'version',
        version = f'{parser.prog} version 0.0.1',
    )
    
    exclusive_group = parser.add_mutually_exclusive_group()

    # selections
    exclusive_group.add_argument(
        '-c', '--conference',
        choices = conferences,
        type = str.lower,
        action = 'extend',
        nargs = '*',
        help = 'group results by CONFERENCE',
        metavar = 'CONFERENCE'
    )

    exclusive_group.add_argument(
        '-d', '--division',
        choices = divisions,
        type = str.lower,
        action = 'extend',
        nargs = '*',
        help = 'group results by DIVISION',
        metavar = 'DIVISION'
    )

    exclusive_group.add_argument(
        '-w', '--wild-card',
        choices = conferences,
        type = str.lower,
        action = 'extend',
        nargs = '*',
        help = 'insert the wild card cut line for CONFERENCE',
        metavar = 'CONFERENCE'
    )

    abvs = [key for key in teams]
    exclusive_group.add_argument(
        '-t', '--team',
        choices = abvs,
        type = str.upper,
        action = 'store',
        nargs = 1,
        help = 'query results for team with ABBREVIATION',
        metavar = 'ABBREVIATION'
    )

    # output formats

    # miscellaneous
    exclusive_group.add_argument(
        '-A', '--abbreviations',
        action = 'store_true',
        help = 'show team abbreviations',
    )
    
    return parser

# TODO create a map for command levels. selection | misc, format
def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()

    if args.conference is not None:
        selected_conferences = []
        if len(args.conference) == 0:
            selected_conferences = conferences
        else:
            [selected_conferences.append(c) for c in args.conference if c not in selected_conferences]
        print(selected_conferences)

    if args.division is not None:
        selected_divisions = []
        if len(args.division) == 0:
            selected_divisions = divisions
        else:
            [selected_divisions.append(c) for c in args.division if c not in selected_divisions]
        print(selected_divisions)

    if args.wild_card is not None:
        selected_conferences = []
        if len(args.wild_card) == 0:
            selected_conferences = conferences
        else:
            [selected_conferences.append(c) for c in args.wild_card if c not in selected_conferences]
        print(selected_conferences)

    if args.team is not None:
        print(args.team)

    if args.abbreviations:
        for i, key in enumerate(teams):
            print(f'{key} - {teams[key]}')

if __name__ == '__main__':
    main()

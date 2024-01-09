import sys
import argparse

from typing import List, Dict, Any
from datetime import datetime

# from standings import Standings
# from players import Players

datetime_today = datetime.now()
today = '{:04d}-{:02d}-{:02d}'.format(
    datetime_today.year,
    datetime_today.month,
    datetime_today.day
)

OptStore = Dict[str, Any]
'''A dict structure that stores the options provided to the program'''

def standings_action(opts: OptStore):
    for k, v in opts.items():
        print(f'{k}: {v}')

    # the order the results are displayed is the difference

def add_default_args(parser: argparse.ArgumentParser):

    parser.set_defaults(func=lambda x: None)

    parser.add_argument(
        '-R',
        '--reverse',
        action='store_true',
        dest='reverse'
    )

    subparsers = parser.add_subparsers()

    standings_parser = subparsers.add_parser('standings')
    standings_parser.set_defaults(func=standings_action)

    standings_group = standings_parser.add_mutually_exclusive_group()

    standings_group.add_argument(
        '-o', 
        '--overall', 
        nargs='?', 
        const=today,
        dest='overall',
        metavar='YYYY-MM-DD',
    )

def _parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    add_default_args(parser)

    # store the options in a data structure
    return parser.parse_args(args)


def main(args: List[str]):

    opts = _parse_args(args)
    opts.func(vars(opts))


if __name__ == '__main__':
    main(sys.argv[1:])

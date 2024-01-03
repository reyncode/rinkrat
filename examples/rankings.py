import argparse

'''
    good reference for argparse project structure:
    git@github.com:pyscaffold/pyscaffold.git
'''

def get_standings(args) -> None:

    # api call

    if args.overall:
        print('sorting in overall order')

    if args.conference:
        print('sorting by conference')

    if args.division:
        print('sorting by division')

    if args.wild_card:
        print('sorting by wild-card')

def parse_args():
    parser = argparse.ArgumentParser(prog = 'prog')

    parser.set_defaults(func = lambda x: None)

    subparsers = parser.add_subparsers()

    standings_parser = subparsers.add_parser('standings')

    standings_group = standings_parser.add_mutually_exclusive_group()
    standings_group.add_argument('-o', '--overall', action = 'store_true')
    standings_group.add_argument('-c', '--conference', action = 'store_true')
    standings_group.add_argument('-d', '--division', action = 'store_true')
    standings_group.add_argument('-w', '--wild-card', action = 'store_true')

    standings_parser.set_defaults(func = get_standings)

    return parser.parse_args()

def main() -> None:
    args = parse_args()

    args.func(args)

if __name__ == '__main__':
    main()

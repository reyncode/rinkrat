import argparse

import order # local

def get_standings(args) -> None:

    # api call

    if args.overall:
        order.order_by_overall()

    if args.conference:
        order.order_by_conference()

    if args.division:
        order.order_by_division()

    if args.wild_card:
        order.order_by_wild_card()

def _parse_args():
    parser = argparse.ArgumentParser(prog = 'rinkrat')

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
    args = _parse_args()

    args.func(args)

if __name__ == '__main__':
    main()

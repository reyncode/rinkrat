import argparse

def main() -> None:

    '''

        rinkrat
        ├── standings 
        │   ├── overall
        │   ├── conference [east, west]
        │   ├── division [atlantic, metro, central, pacific]
        │   └── wild-card [east, west]
        ├── team 
        │   ├── roster [abbreviation]
        │   └── stats [abbreviation]
        ├── leaders
        │   ├── goals
        │   ├── assists
        │   ├── points
        │   ├── goals-against-average
        │   ├── save-percentage
        │   └── wins
        └── player
            ├── about [name]
            └── stats [name]

    '''

    parser = argparse.ArgumentParser(prog = 'mutuals')

    subparsers = parser.add_subparsers()

    team_parser = subparsers.add_parser('team')
    player_parser = subparsers.add_parser('player')
    standings_parser = subparsers.add_parser('standings')
    leaders_parser = subparsers.add_parser('leaders')

    # teams
    team_group = team_parser.add_mutually_exclusive_group()
    team_group.add_argument('-r', '--roster')
    team_group.add_argument('-s', '--stats')

    # players
    player_group = player_parser.add_mutually_exclusive_group()
    player_group.add_argument('-a', '--about')
    player_group.add_argument('-s', '--stats')

    # standings
    standings_group = standings_parser.add_mutually_exclusive_group()
    standings_group.add_argument('-o', '--overall', action = 'store_true')
    standings_group.add_argument('-c', '--conference', action = 'store_true')
    standings_group.add_argument('-d', '--division', action = 'store_true')
    standings_group.add_argument('-w', '--wild-card', action = 'store_true')

    # player leaders
    leaders_group = leaders_parser.add_mutually_exclusive_group()
    leaders_group.add_argument('-g', '--goals', action = 'store_true')
    leaders_group.add_argument('-a', '--assists', action = 'store_true')
    leaders_group.add_argument('-p', '--points', action = 'store_true')
    leaders_group.add_argument('-w', '--wins', action = 'store_true')
    leaders_group.add_argument('-o', '--gaa', action = 'store_true')

    # base options
    parser.add_argument('-R', '--reverse', action = 'store_true')
    parser.add_argument('-n', '--lines')

    args = parser.parse_args()

    print(args)

if __name__ == '__main__':
    main()

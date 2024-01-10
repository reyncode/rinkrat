import argparse
import sys
from typing import List

from commands import standings, team

class Cli:
    def __init__(self, argv: List[str]) -> None:
        self.argv = argv

        parser = argparse.ArgumentParser()

        parser.add_argument("command")

        args = parser.parse_args(argv[:1])

        # connect the constructor to the attribute
        setattr(self, "standings", standings.Standings)
        setattr(self, "team", team.Team)

        try:
            # run the constructor for the command of the invoked attribute
            getattr(self, args.command)(argv[1:])
        except AttributeError:
            print(f"{args.command} is not a valid command.")
            parser.print_help()

def main(argv: List[str]):
    Cli(argv)

if __name__ == "__main__":
    # chop the program name out of the argument list
    main(sys.argv[1:])

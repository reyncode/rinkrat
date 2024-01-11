import argparse
import sys
from typing import List

from commands import standings, team

usage_str = """rinkrat <command> [<args>]

commands:
  standings  Show the team rankings in a specified format.
  team       Show information for a specific team.
"""

class Cli:
    def __init__(self, argv: List[str]) -> None:
        # create an attribute that points to the command's constructor
        setattr(self, "standings", standings.Standings)
        setattr(self, "team", team.Team)

        parser = argparse.ArgumentParser(
            usage=usage_str
        )

        parser.add_argument("command")

        args = parser.parse_args(argv[:1])

        try:
            # invoke the constructor of the selected command and pass the relevant args
            getattr(self, args.command)(argv[1:])
        except AttributeError:
            print(f"\"{args.command}\" is not a valid command.", end="\n\n")
            parser.print_help()

def main(argv: List[str]):
    Cli(argv)

if __name__ == "__main__":
    # don't include the name of the program
    main(sys.argv[1:])

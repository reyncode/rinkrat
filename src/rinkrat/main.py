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
    def __init__(self) -> None:
        # create an attribute that points to the command's constructor
        setattr(self, "standings", standings.Standings)
        setattr(self, "team", team.Team)

        self.parser = argparse.ArgumentParser(prog="rinkrat", usage=usage_str)
        self.parser.add_argument("command")

    def run(self, argv: List[str]) -> None:
        args = self.parser.parse_args(argv[:1])

        try:
            getattr(self, args.command)(argv[1:])
            # ^ invoke the relevant constructor with the users args
        except AttributeError:
            invalid = f"\"{args.command}\" is not a valid command, see --help"

            argparse.ArgumentParser.error(
                self=self.parser,
                message=invalid)


def main(argv: List[str]):
    cli = Cli()
    cli.run(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
    # ^ don't include the name of the program

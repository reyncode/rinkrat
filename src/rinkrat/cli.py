import argparse
import sys
from typing import List, Dict, Any

from . import standings

usage_str = """rinkrat <command> [<args>]

commands:
  standings  show the team rankings in a specified format
"""

class Cli:
    def __init__(self) -> None:
        # create an attribute that points to the command's constructor
        setattr(self, "standings", standings.Standings)

        self.parser = argparse.ArgumentParser(prog="rinkrat", usage=usage_str)
        self.parser.add_argument("command")

    def parse(self, argv: List[str]) -> Dict[str, Any]:
        """
        package our args into a dict
        """

        args = self.parser.parse_args(argv[:1])

        if not hasattr(self, args.command):
            invalid = f"\"{args.command}\" is not a valid command, see --help"

            argparse.ArgumentParser.error(
                self=self.parser,
                message=invalid)

        opts = vars(args)

        opts["argv"] = argv
        opts["constructor"] = getattr(self, args.command)

        return opts

def execute(opts: Dict[str, Any]):
    """
    execute the command that has been parsed with the collected args
    """

    obj = opts["constructor"]()
    argv = opts["argv"]

    obj.parse(argv[1:])
    obj.execute()

def main(argv: List[str]):
    cli = Cli()
    opts = cli.parse(argv)

    execute(opts)

if __name__ == "__main__":
    main(sys.argv[1:])
    # ^ don't include the name of the program

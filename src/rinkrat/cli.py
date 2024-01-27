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
        Parses the passed argument vector and stores the results
        inside of a dict that can be passed to execute().
        """
        args = self.parser.parse_args(argv[:1])

        if not hasattr(self, args.command):
            invalid = f"\"{args.command}\" is not a valid command, see --help"

            argparse.ArgumentParser.error(
                self=self.parser,
                message=invalid)

        opts = vars(args)

        # TODO - make this a field of cli
        opts["argv"] = argv
        opts["constructor"] = getattr(self, args.command)

        return opts

    def execute(self, opts: Dict[str, Any]):
        """
        Perform the actions associated with the stored argument.
        """
        obj = opts["constructor"]()
        argv = opts["argv"]

        obj.parse(argv[1:])
        obj.execute()

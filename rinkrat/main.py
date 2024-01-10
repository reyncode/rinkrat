import argparse
import sys
from typing import List

class Cli:
    def __init__(self, argv: List[str]) -> None:
        self.argv = argv

        parser = argparse.ArgumentParser(
            usage="rinkrat <command> [<args>]"
        )

        parser.add_argument("command", help="rinkrat commands")

        args = parser.parse_args(argv[:1])

        try:
            getattr(self, args.command)()
        except AttributeError:
            parser.print_help()

    def test(self):
        parser = argparse.ArgumentParser(description="prints a string")
        parser.add_argument("-t", "--test", required=True, dest="string", help="the test option")

        args = parser.parse_args(self.argv[1:])

        test_action(args.string)


def test_action(string):
    print(string)

def main(argv: List[str]):
    Cli(argv)

if __name__ == "__main__":
    main(sys.argv[1:])

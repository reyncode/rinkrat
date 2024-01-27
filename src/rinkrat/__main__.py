import sys as _sys
from typing import List

from . import cli

def main(argv: List[str]) -> None:
    interface = cli.Cli()

    interface.parse(argv)
    interface.execute()

if __name__ == "__main__":
    main(_sys.argv[1:])
    # ^ don't include the name of the program

import argparse
from typing import List

date = "2024-01-10"

def fake_api_call():
    return {}

class Standings:
    def __init__(self, argv: List[str]) -> None:

        parser = argparse.ArgumentParser(description="The standings argument parser")

        group = parser.add_mutually_exclusive_group()

        group.add_argument(
            "-o",
            "--overall",
            nargs="?",
            const=date,
            dest="overall",
            help="overall team standings"
        )

        group.add_argument(
            "-c",
            "--conference",
            nargs="?",
            const=date,
            dest="conference",
            help="conference team standings"
        )
        
        # create a dictionary of the selected options
        self.opts = vars(parser.parse_args(argv))

        print(self.opts)

        # validate

        # api call
        self.opts.setdefault("data", fake_api_call())

        self.order()
        self.display()

    def order(self):
        if self.opts["overall"] is not None:
            print(self.opts["overall"])

        if self.opts["conference"] is not None:
            print(self.opts["conference"])


    def display(self):
        print(f"doing the display for Standings")



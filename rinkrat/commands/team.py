import argparse

from typing import List

def fake_api_call():
    return {}

class Team:
    def __init__(self, argv: List[str]) -> None:
        parser = argparse.ArgumentParser(description="The team argument parser")

        group = parser.add_mutually_exclusive_group()

        group.add_argument(
            "-r",
            "--roster",
            dest="roster",
            help="Active roster for TEAM"
        )

        group.add_argument(
            "-s",
            "--stats",
            dest="stats",
            help="Stats for for TEAM"
        )

        # create a dictionary of the selected options
        self.opts = vars(parser.parse_args(argv))

        # api call
        self.opts.setdefault("data", fake_api_call())

        self.display()

        print(self.opts)

    def display(self):
        if self.opts["roster"] is not None:
            print(f"Displaying roster for {self.opts['roster']}")

        if self.opts["stats"] is not None:
            print(f"Displaying stats for {self.opts['stats']}")

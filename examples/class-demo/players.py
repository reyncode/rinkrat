from subcommand import Subcommand

players_url = 'www.players.com/players/player1'

class Players(Subcommand):
    def __init__(self, args) -> None:
        super().__init__(args)

    def run(self):
        super()._get(players_url)
        self._order()
        self.display()

    def _order(self):
        print('Players: placing the results in order')

    def display(self):
        print('Players: doing Players version of display, using \'{}\' args'.format(self.args))


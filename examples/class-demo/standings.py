from subcommand import Subcommand

standings_url = 'www.standings.com/standings/now'

class Standings(Subcommand):
    def __init__(self, args) -> None:
        super().__init__(args)

    def run(self):
        super()._get(standings_url)
        self._order()
        self.display()

    def _order(self):
        print('Standings: placing the results in order')

    def display(self):
        print('Standings: doing Standings version of display, using \'{}\' args'.format(self.args))

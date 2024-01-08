from standings import Standings
from players import Players

def main():
    standings = Standings('my args')
    standings.run()
    
    players = Players('main args')
    players.run()


if __name__ == '__main__':
    main()

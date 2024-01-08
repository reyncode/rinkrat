from api import get_request

# superclass for the sub commands
class Subcommand():

    def __init__(self, args) -> None:
        self.args = args
        print(args)

    def _get(self, url):
        get_request(url)
        
    # enforce custom implementaion of display
    def display(self):
        raise NotImplementedError

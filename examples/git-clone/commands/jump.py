import sys
import argparse

class Jump(object):
    def __init__(self, parser: argparse.ArgumentParser) -> None:
        subparser_action = parser.add_subparsers()

        subparser = subparser_action.add_parser(name='jump_subparser')

        subparser.add_argument('-i','--high', dest='jump_high', help='high jump')
        subparser.add_argument('-l','--low', dest='jump_low', help='low jump')

        args = subparser.parse_args()

        print(args)

def action(parser: argparse.ArgumentParser):
    parser = argparse.ArgumentParser(description='How high did you jump?')
    parser.add_argument('-n','--height', dest='height', help='height of the jump')

    # we could instead pass sys.argv[2:] to a constructor and store the attr
    args = parser.parse_args(sys.argv[2:])

    jump(args.height)

def jump(height):
    print(f'you jumped {height} high')
    

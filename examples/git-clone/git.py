import argparse
import sys

from commands import jump

def say_hi():
    print('hi')

class GitMaster(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
        usage='''git <command> [<args>]
                The git commands are:
                add    Add a file from working directory to the staging area.
                commit Commit a file from staging area to the local repository.
         ''')

        parser.add_argument('command', help='git commands')

        parser.add_argument('-v', '--version', help='show version and exit', action='version', version='1.0')
        
        # Read the first argument (add/commit)
        args = parser.parse_args(sys.argv[1:2])

        print(args)

        # use setattr to pace commands in their own folders
        setattr(self, 'jump', jump.action)

        # setattr(self, 'jump', jump.Jump)

        # Use dispatch pattern to invoke method with same name of the argument
        try:
            getattr(self, args.command)(parser)
        except AttributeError as e:
            print(e)
            parser.print_help()

    # these get moved into separate files
    def add(self):
        parser = argparse.ArgumentParser(description='Adds a file')
        parser.add_argument('-f','--file-name', required=True, dest='filename', help='file to be added')

        # We are inside a subcommand, so ignore the first argument and read the rest
        args = parser.parse_args(sys.argv[2:])
        git_add(args.filename)

    def commit(self):
        parser = argparse.ArgumentParser(description='Commits a file')
        parser.add_argument('-m','--comment', required=True, dest='comment', help='comment to be used for commit')

        # We are inside a subcommand, so ignore the first argument and read the rest
        args = parser.parse_args(sys.argv[2:])
        git_commit(args.comment)


# Dummy Functions
def git_add(filename):
    # Write the required logic for the action “add”
     print ('Inside add action')
     print ('Passed file name is %s'.format(filename))

def git_commit(comment):
    # Write the required logic for the action “commit”
     print ('Inside comment action')
     print ('Passed comment is %s'.format(comment))

if __name__ == '__main__':
    # pass sys.args for readability
    GitMaster()

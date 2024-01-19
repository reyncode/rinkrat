import pytest

from rinkrat import main

'''
    main.py unit test

    - passing an invalid command raises an exception and ends the program

'''

def test_cli_has_command_attrs():
    """
    ensure the cli has assigned the command name as an attribute.
    """
    attrs = ["standings"]

    cli = main.Cli()

    for attr in attrs:
        assert hasattr(cli, attr)

def test_cli_exit_on_bad_command():
    pass

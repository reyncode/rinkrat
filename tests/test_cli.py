import pytest

from rinkrat import cli

@pytest.fixture
def _cli() -> cli.Cli:
    return cli.Cli()

def test_cli_has_command_attrs(_cli):
    """
    ensure the cli has assigned the command name as an attribute.
    """
    attrs = ["standings"]

    for attr in attrs:
        assert hasattr(_cli, attr)

def test_cli_exit_on_bad_command(_cli):
    args = ["nothing"]

    with pytest.raises(SystemExit):
        _cli.parse(args)

def test_cli_calling_execute_before_parse(_cli):
    """
    the application should throw a system exit if the programmer tries
    to call the execute method before calling parse
    """
    with pytest.raises(SystemExit):
        _cli.execute()


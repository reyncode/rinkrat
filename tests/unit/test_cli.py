import pytest

from rinkrat import cli

def test_cli_has_command_attrs():
    """
    ensure the cli has assigned the command name as an attribute.
    """
    attrs = ["standings"]

    obj = cli.Cli()

    for attr in attrs:
        assert hasattr(obj, attr)

def test_cli_exit_on_bad_command():
    args = ["nothing"]

    obj = cli.Cli()

    with pytest.raises(SystemExit):
        obj.parse(args)


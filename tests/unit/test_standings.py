import pytest

from rinkrat import standings

@pytest.fixture
def _standings() -> standings.Standings:
    return standings.Standings()

def test_standings_has_ranking_attrs(_standings):
    """
    does the object have callable attributes set for each ranking
    """
    attrs = ["overall", "conference", "division", "wild"]

    for attr in attrs:
        assert hasattr(_standings, attr)

def test_standings_exit_on_bad_ranking(_standings):
    """
    does the program raise a SystemExit when a bad ranking is passed
    """
    args = ["invalid"]

    with pytest.raises(SystemExit):
        _standings.parse(args)

def test_standings_ranking_exit_on_bad_args(_standings):
    """
    does the program raise a SystemExit when an invalid argument is passed
    to a ranking
    """
    args = {
        "overall": ["space"],
        "conference": ["northern", "western"],
        "division": ["atlantic", "mythic"],
        "wild": ["scandinavia"],
    }

    for k, v in args.items():
        with pytest.raises(SystemExit):
            argv = [k]
            [argv.append(a) for a in v]

            _standings.parse(argv)
            _standings.execute()

def test_standings_ranking_default_selection(_standings):
    """
    does the object contain the expected selections when defaults are used
    for the ranking
    """
    defaults = {
        "overall": ["overall"],
        "conference": ["eastern", "western"],
        "division": ["atlantic", "metropolitan", "central", "pacific"],
        "wild": ["eastern", "western"],
    }

    for ranking in defaults.keys():
        _standings.parse([ranking])
        _standings.execute()
        assert defaults[ranking] == _standings.opts["selection"]

def test_standings_is_valid_query_date():
    """
    does the function return true for the accepted format and false
    otherwise
    """
    assert standings.is_valid_query_date("2010-12-31") == True
    assert standings.is_valid_query_date("12.345/6789") == False

def test_standings_exit_on_bad_date():
    """
    does the program exit with a SystemExit if a bad date is passed to -d
    """
    args = ["overall", "-d", "785-8993.abcd,*&^%"]

    obj = standings.Standings()

    with pytest.raises(SystemExit):
        obj.parse(args)
        obj.execute()

    

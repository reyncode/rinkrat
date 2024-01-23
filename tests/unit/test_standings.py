import pytest

from rinkrat import standings

def test_standings_has_ranking_attrs():
    """
    does the object have callable attributes set for each ranking
    """
    attrs = ["overall", "conference", "division", "wild"]

    obj = standings.Standings()

    for attr in attrs:
        assert hasattr(obj, attr)

def test_standings_exit_on_bad_ranking():
    """
    does the program raise a SystemExit when a bad ranking is passed
    """
    args = ["invalid"]

    obj = standings.Standings()

    with pytest.raises(SystemExit):
        obj.parse(args)

def test_standings_ranking_exit_on_bad_args():
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

    obj = standings.Standings()

    for k, v in args.items():
        with pytest.raises(SystemExit):
            argv = [k]
            [argv.append(a) for a in v]

            obj.parse(argv)
            obj.execute()

def test_standings_ranking_default_selection():
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

    obj = standings.Standings()

    for ranking in defaults.keys():
        obj.parse([ranking])
        obj.execute()
        assert defaults[ranking] == obj.opts["selection"]

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

    

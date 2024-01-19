import pytest

from rinkrat import standings

def test_standings_has_ranking_attrs():
    attrs = ["overall", "conference", "division", "wild"]

    obj = standings.Standings()

    for attr in attrs:
        assert hasattr(obj, attr)

def test_standings_exit_on_bad_ranking():
    args = ["invalid"]

    obj = standings.Standings()

    with pytest.raises(SystemExit):
        obj.parse(args)

def test_standings_ranking_exit_on_bad_args():
    args = {
        "overall": ["overall", "additional"], # no additional args accepted
        "conference": ["conference", "invalid"],
        "division": ["division", "invalid"],
        "wild": ["wild", "invalid"],
    }

    obj = standings.Standings()

    for value in args.values():
        with pytest.raises(SystemExit):
            obj.parse(value)

def test_standings_ranking_default_selection():
    defaults = {
        "overall": ["overall"],
        "conference": ["eastern", "western"],
        "division": ["atlantic", "metropolitan", "central", "pacific"],
        "wild": ["eastern", "western"],
    }

    obj = standings.Standings()

    for ranking in defaults.keys():
        obj.parse([ranking])
        assert defaults[ranking] == obj.opts["selection"]

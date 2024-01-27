import pytest

from rinkrat import standings
from data import data

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
    assert standings._is_valid_query_date("2010-12-31") == True
    assert standings._is_valid_query_date("12.345/6789") == False

def test_standings_exit_on_bad_date(_standings):
    """
    does the program exit with a SystemExit if a bad date is passed to -d
    """
    args = ["overall", "-d", "785-8993.abcd,*&^%"]

    with pytest.raises(SystemExit):
        _standings.parse(args)
        _standings.execute()

def test_standings_ranking_overall():
    result = standings._ranked_overall(data.teams_2023_12_31)

    for i, team in enumerate(result["Overall"]):
        assert data.overall_2023_12_31[i] == team.get('teamName').get('default')
        
def test_standings_ranking_eastern_conference():
    result = standings._ranked_conference(["eastern"], data.teams_2023_12_31)

    for i, team in enumerate(result["Eastern"]):
        assert data.eastern_conference_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_ranking_western_conference():
    result = standings._ranked_conference(["western"], data.teams_2023_12_31)

    for i, team in enumerate(result["Western"]):
        assert data.western_conference_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_ranking_atlantic_division():
    result = standings._ranked_division(["atlantic"], data.teams_2023_12_31)

    for i, team in enumerate(result["Atlantic"]):
        assert data.atlantic_division_2023_12_31[i] == team.get('teamName').get('default')
    
def test_standings_ranking_metropolitan_division():
    result = standings._ranked_division(["metropolitan"], data.teams_2023_12_31)

    for i, team in enumerate(result["Metropolitan"]):
        assert data.metropolitan_division_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_ranking_central_division():
    result = standings._ranked_division(["central"], data.teams_2023_12_31)

    for i, team in enumerate(result["Central"]):
        assert data.central_division_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_ranking_pacific_division():
    result = standings._ranked_division(["pacific"], data.teams_2023_12_31)

    for i, team in enumerate(result["Pacific"]):
        assert data.pacific_division_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_ranking_eastern_wildcard():
    result = standings._ranked_wild(["eastern"], data.teams_2023_12_31)

    for i, team in enumerate(result["Eastern"]):
        assert data.eastern_wildcard_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_ranking_western_wildcard():
    result = standings._ranked_wild(["western"], data.teams_2023_12_31)

    for i, team in enumerate(result["Western"]):
        assert data.western_wildcard_2023_12_31[i] == team.get('teamName').get('default')

def test_standings_call_execute_without_parsing(_standings):
    with pytest.raises(SystemExit):
        _standings.execute()

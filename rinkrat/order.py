'''
Methods in this file handle the ordering of the api results.
'''

from typing import List

def order_by_overall(teams: List) -> dict:
    overall = []

    for team in teams:
        overall.append(team)

    result = dict()
    result['league'] = overall

    return result

def order_by_conference(teams: List) -> dict:
    eastern = []
    western = []

    for team in teams:
        
        if team['conferenceName'] == 'Eastern':
            eastern.append(team)

        elif team['conferenceName'] == 'Western':
            western.append(team)

    result = dict()
    result['eastern'] = eastern
    result['western'] = western

    return result

def order_by_division(teams: List) -> dict:
    atlantic = []
    metropolitan = []
    central = []
    pacific = []

    for team in teams:

        if team['divisionName'] == 'Atlantic':
            atlantic.append(team)

        elif team['divisionName'] == 'Metropolitan':
            metropolitan.append(team)

        elif team['divisionName'] == 'Central':
            central.append(team)

        elif team['divisionName'] == 'Pacific':
            pacific.append(team)

    result = dict()
    result['atlantic'] = atlantic
    result['metropolitan'] = metropolitan
    result['central'] = central
    result['pacific'] = pacific

    return result

def order_by_wild_card(teams: List) -> dict:
    atlantic = []
    metropolitan = []
    central = []
    pacific = []
    wild_card_east = []
    wild_card_west = []

    for team in teams:

        if team['divisionName'] == 'Atlantic' and team['wildcardSequence'] == 0:
            atlantic.append(team)

        elif team['divisionName'] == 'Metropolitan' and team['wildcardSequence'] == 0:
            metropolitan.append(team)
        
        elif team['divisionName'] == 'Central' and team['wildcardSequence'] == 0:
            central.append(team)
        
        elif team['divisionName'] == 'Pacific' and team['wildcardSequence'] == 0:
            pacific.append(team)
        
        elif team['conferenceName'] == 'Eastern':
            wild_card_east.append(team)
        
        elif team['conferenceName'] == 'Western':
            wild_card_west.append(team)

    result = dict()

    result['atlantic'] = atlantic
    result['metropolitan'] = metropolitan
    result['wild_card_east'] = wild_card_east
    result['central'] = central
    result['pacific'] = pacific
    result['wild_card_west'] = wild_card_west

    return result

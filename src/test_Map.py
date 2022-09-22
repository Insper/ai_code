from Map import *

Map.createArea()
Map.createHeuristics()


def test_is_goal_retorna_corretamente_0():
    print('\n#### Test metodo is_goal retorna corretamente 0 ####')
    state = Map('i', 0, 'i', 'x')
    assert state.is_goal() == False

def test_is_goal_retorna_corretamente_1():
    print('\n#### Test metodo is_goal retorna corretamente 1 ####')
    state = Map('i', 0, 'i', 'i')
    assert state.is_goal() == True

def test_successors_retorna_corretamente():
    print('\n#### Test metodo successors retorna sucessores corretamente ####')
    state = Map('i', 0, 'i', 'x').sucessors()
    expected_values = [
        {'city': 'e', 'cost_value': 2, 'operator': 'e', 'goal': 'x'},
        {'city': 'h', 'cost_value': 2, 'operator': 'h', 'goal': 'x'}
    ]
    for i in range(len(expected_values)):
        assert expected_values[i] == state[i].__dict__

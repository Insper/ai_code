from Map import *
from aicode.search.SearchAlgorithms import AEstrela

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

def test_algoritmo_encontra_solucao_existente():
    print('\n#### Teste algoritmo encontra solucao que existe ####')
    state = Map('i', 0, 'i', 'x')
    algorithm = AEstrela()
    res = algorithm.search(state)
    assert res != None

def test_algoritmo_encontra_melhor_solucao_possivel_a_o():
    print('\n#### Teste algoritmo encontra solucao de a para o ####')
    state = Map('a', 0, 'a', 'o')
    algorithm = AEstrela()
    res = algorithm.search(state)
    assert res.g == 8

def test_algoritmo_encontra_melhor_solucao_possivel_n_x():
    print('\n#### Teste algoritmo encontra solucao de n para x ####')
    state = Map('n', 0, 'n', 'x')
    algorithm = AEstrela()
    res = algorithm.search(state)
    assert res.g == 3

from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from U2 import U2

def test_menor_caminho():
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g <= 17
    print(result.show_path())

def test_sem_solucao_01():
    state = U2(True, True, True, True, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result == None

def test_sem_solucao_02():
    state = U2(False, False, False, False, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result == None

def test_custo_excedente():
    state = U2(False, False, False, True, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g > 17
    print(result.show_path())


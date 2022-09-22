from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from U2 import U2

def test_menor_caminho():
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g <= 17
    print(result.show_path())

def test_solucao_inviavel():
    """
    Considerando que todos os integrantes estão do lado
    esquerdo da ponte e a lanterna do lado direito
    """
    state = U2(False, False, False, False, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result == None

def test_solucao_inviavel2():
    """
    Considerando que todos os integrantes estão do lado
    direito da ponte e a lanterna do lado esquerdo
    """
    state = U2(True, True, True, True, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result == None

def test_tempo_excedente():
    """
    Considerando que o mais lento (Larry) está
    do lado direito da ponte com a lanterna e o
    restante do lado esquerdo
    """
    state = U2(False, False, False, True, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g>17
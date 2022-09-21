from aicode.search.SearchAlgorithms import *
from VacuumWorld import *

'''
Testes usando o meio mais simples VacuumWorld
'''

def test_busca_largura():
    state = VacuumWorld('right', True, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result:
        print(result.show_path())
    else:
        print('Sem solucao')
    assert result.g != None
    print(result.show_path())

def test_busca_profundidade():
    state = VacuumWorld('right', True, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result:
        print(result.show_path())
    else:
        print('Sem solucao')
    assert result.g != None
    print(result.show_path())

def teste_custo_uniforme():
    state = VacuumWorld('right', True, False, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result:
        print(result.show_path())
    else:
        print('Sem solucao')
    assert result.g != None
    print(result.show_path())







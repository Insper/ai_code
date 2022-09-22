from aicode.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaProfundidadeIterativa
from VacuumWorld import VacuumWorld
from ProblemSpecificationExample import ProblemSpecification
from aicode.search.Graph import State

def test_BuscaLargura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != 0

def test_BuscaProfundidade():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 300)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != 0

def test_BuscaProfundidadeIterativa():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != 0
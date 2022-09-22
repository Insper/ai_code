from collections import deque
from aicode.search.Graph import Node
import logging
logging.basicConfig(filename='search_algorithms.log', level=logging.DEBUG)
from aicode.search.SearchAlgorithms import *
from VacuumWorld import *

def test_largura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; clean ; Move Left ; clean"


def test_profundidade():
    state = VacuumWorld('left', False, True, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 20)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; clean"
    
def test_BPI2():
    state = VacuumWorld('left', True, True, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == ""
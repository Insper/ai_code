from re import T
import re
# from turtle import st
from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from U2 import U2

def test_menor_caminho():
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g <= 17
    print(result.show_path())

def test_laterna_sozinha():
    state = U2(False, False, False, False, True, ' ')
    algorith = BuscaCustoUniforme()
    result = algorith.search(state)
    assert result == None
    

def test_todos_no_final():
    state = U2(True, True, True, True, False, ' ')
    algorith = BuscaCustoUniforme()
    result = algorith.search(state)
    assert result == None  

def test_mais_rapido_caminho():
    state = U2(False, True, True, True, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g == 1
    print(result.show_path())

test_todos_no_final()
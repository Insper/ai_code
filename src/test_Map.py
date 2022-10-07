#Quando quiser saber o caminho, passar a flag -s para o pytest
#pytest -s src/test_Map.py

from aicode.search.SearchAlgorithms import AEstrela
import time 
from Map import *

Map.createHeuristics()
Map.createArea()

def test_a_x():
    state = Map('a',0, 'a','x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')    
    assert result.g == 12
    print(result.show_path())
    

def test_menor_caminho_n_ate_x():
    state = Map('n', 0, 'n', 'x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 3
    print(result.show_path()) 

def test_b_x():
    state = Map('b',0, 'b','x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 9
    print(result.show_path())


def test_menor_caminho_l_ate_o():
    state = Map('l', 0, 'l', 'o')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 11
    print(result.show_path())


def test_c_o():
    state = Map('c',0, 'c','o')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 2

def test_menor_caminho_x_ate_o():
    state = Map('x', 0, 'x', 'o')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 16
    print(result.show_path())
from aicode.search.SearchAlgorithms import AEstrela
import time
from Map import *

Map.createArea()
Map.createHeuristics()

def test_menor_caminho_d_ate_o():    
    state = Map('f', 0, 'f', 'o')       #primeiro,0,primeiro,ultimo
    algorithm = AEstrela()
    #algorithm = BuscaCustoUniforme()
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
    assert result.g == 5
    print(result.show_path())

def test_menor_caminho_e_ate_x():
    state = Map('e', 0, 'e', 'x')     #primeiro,0,primeiro,ultimo
    algorithm = AEstrela()
    #algorithm = BuscaCustoUniforme()
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
    assert result.g == 14
    print(result.show_path())

def test_menor_caminho_k_ate_o():
    state = Map('k', 0, 'k', 'o')   #primeiro,0,primeiro,ultimo
    algorithm = AEstrela()
    #algorithm = BuscaCustoUniforme()
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
    assert result.g == 10
    print(result.show_path())
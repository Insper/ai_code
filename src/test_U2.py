from operator import truediv
from aicode.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura,BuscaProfundidadeIterativa,BuscaProfundidade,BuscaGananciosa,AEstrela
from U2 import U2

    #Para bono, edge, adam, larry e lanterna FALSE significa lado esquerdo do rio
    #TRUE significa lado direito do rio
    #Tem que passar do lado esquerdo pro direito

def test_menor_caminho():
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g <= 17

def test_custo_elevado():
    "Teste em que a pessoa que possui o maior custo começa a lanterna fazendo com que a banda chegue atrasada ao concerto"
    state = U2(False, False, False, True, True,'')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g >= 17

def test_resolvido():
    "Teste em que o problema ja começa resolvido, ou seja, todos já estão do lado certo da ponte então o custo é 0"
    state = U2(True, True, True, True, True, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g == 0


def test_sem_solucao():
    "Teste em que ninguem consegue atravessar a ponte pois a lanterna está do outro lado"
    state = U2(False, False, False, False, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result == None

def test_do_menos_veloz():
    "Teste para verificar se o custo para duas pessoas atravessarem ao mesmo tempo é igual ao custo do menos veloz"

    "Larry + Bono = 10"
    state = U2(False, True, True, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g == 10

    "edge + adam = 5"
    state = U2(True, False, False, True, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g == 5

def test_algorithm_BuscaLargura():
    state = U2(False, False, False, False, False,'')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    assert result.g >= 17

def test_algorithm_BuscaProfundidade():
    state = U2(False, False, False, False, False,'')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state,200)
    assert result.g >= 17

def test_algorithm_BuscaProfundidadeI():
    state = U2(False, False, False, False, False,'')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    assert result.g >= 17

    
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
    print(result.show_path())

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

def test_larry():
    '''
        Este teste leva em consideração que o integrante mais lento da banda é o unico que se
        encontra do lado da ponte em que esta a lampada, tornando então o tempo de resolução do
        problema maior do que o tempo em que os mesmos tem para chegar ao show.
    '''

    state = U2(False, False, False, False, True, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    assert result.g > 17

def test_lado_direito():
    '''
        Este teste faz a consideração que todos os membros da banda se encontram do lado direito
        da ponte, enquanto a lanterna esta do lado esquerdo, tornando então a solução impossivel. 
    '''

    state = U2(True, True, True, True, True, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    assert result == None
    
def test_lado_esquerdo():
    '''
        Este teste faz a consideração que todos os membros da banda se encontram do lado esquerdo
        da ponte, enquanto a lanterna esta do lado direito, tornando então a solução impossivel. 
    '''

    state = U2(False, False, False, False, False, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    assert result == None

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

from typing import List
from pandas._libs.hashtable import Vector
import requests


def soma_vetores(v, w):
    assert len(v) == len(w) # vetores necessitam ter mesmo tamanho
    return [v_i + w_i for v_i, w_i in zip(v,w)]

print(soma_vetores([1,2,3], [4,5,6]))

def subtracao_vetores(v, w):
    assert  len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

print(subtracao_vetores([1,2,3], [4,5,6]))

def soma_vetores(vectors: List[Vector]):
    assert vectors, "vem vetores providos"
    numero_elemntos = len(vectors[0])
    assert all(len(v) == numero_elemntos for v in vectors), "tamanhos diferentes"
    # o elemento de nº i do resultado é a soma de todoo vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(numero_elemntos)]

print(soma_vetores([[1, 2], [3, 4]]))


requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic= requisicao.json()

cotacao = requisicao_dic["USDBRL"]["bid"]
cotacao = float(cotacao)
assert cotacao>0
print(cotacao)
preco_produto= 10
preco_brl = cotacao*preco_produto
print(preco_brl)

def multiplicacao_escalar(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

def media_componentes(vetores: List[Vector]) -> Vector:
    n = len(vetores)
    return multiplicacao_escalar(1/n, soma_vetores(vetores))

assert media_componentes([[1,2],[3,4],[5,6]]) == [3,4]

#produto escalar de 2 vetores, multiplicação elemento a elemento e soma dessas multiplicações
def produto_escalar(v1: Vector, v2: Vector):
    assert len(v1) == len(v2), "Vetores necessitam ser de mesmo tamanho"
    return sum(v_1 * v_2 for v_1, v_2 in zip(v1, v2)) #Percorre v_1 e v_2 em v1 e v2

print(produto_escalar([1,3,9],[16, 25, 36]))


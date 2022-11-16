from typing import Tuple, Callable

from numpy import matrix
from pandas._libs.hashtable import Vector


def forma(A: matrix) -> Tuple[int, int]:
    num_linhas = len(A)
    num_colunas = len(A[0]) #if A else 0 #executa se A !=0
    return num_linhas, num_colunas

print(forma([[1,2,3], [9,8,7]]))

def retorn_linha(A: matrix, i: int) ->Vector:
    return (A[i])

def retorna_coluna(A: matrix, c: int) ->Vector:
    return [A_i[c] for A_i in A]

def constroi_matriz(num_rows:int,  num_cols: int, entrada: Callable[[int, int], float]) -> matrix:

    return [[entrada(i, j) # com i, crie uma lista
              for j in range(num_cols)] # [entry_fn(i, 0), ... ]
            for i in range(num_rows)] # crie uma lista para cada i

def identidade(n: int) -> matrix:
    # retorna identidade
    return constroi_matriz(n, n, lambda i, j: 1 if i==j else 0)

print(identidade(3))

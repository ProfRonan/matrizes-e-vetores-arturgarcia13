"""Módulo com as funções de manipulação de vetores."""
from tipos import Vetor, Escalar, Matriz

def norma(x: Vetor) -> Escalar | None:
    """Calcula a norma de um vetor"""
    if x == []:
        return None
    
    sum = float()

    for ele in x:
        sum += ele ** 2
    result = sum**(1 / 2)
    return result


def soma(x: Vetor, y: Vetor) -> Vetor | None:
    """Soma dois vetores"""
    if len(x) != len(y):
        return None
    
    result = [0 for _ in range(x)]

    for i, ele_x in enumerate(x):
        result[i] = ele_x + y[i]


def multiplicação_por_escalar(vetor: Vetor, escalar: Escalar) -> Vetor:
    """Multiplica um vetor por um escalar"""
    # TODO: implementar
    # a multiplicação de um vetor [1, 2, 4] por um escalar 2 é [2, 4, 8]
    


def produto_interno(x: Vetor, y: Vetor) -> Escalar | None:
    """Calcula o produto interno de dois vetores"""
    # TODO: implementar
    # o produto interno de dois vetores [1, 2, 4] e [2, 3, 4] é 24
    # o produto interno consiste em multiplicar os elementos de mesmo índice e somar os resultados
    # a multiplicação só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    # caso os vetores sejam vazios o resultado é 0


def produto_vetorial(x: Vetor, y: Vetor) -> Vetor | None:
    """Calcula o produto vetorial de dois vetores"""
    # TODO: implementar
    # o produto vetorial de dois vetores [1, 2, 4] e [2, 3, 4] é [-4, 4, -1]
    # o produto vetorial só pode ser realizado se os vetores tem 3 elementos.
    # caso contrário, deve retornar None


def produto_diádico(x: Vetor, y: Vetor) -> Matriz | None:
    """Calcula o produto diádico de dois vetores"""
    # TODO: implementar
    # o produto diádico de dois vetores [1, 2, 4] e [2, 3, 4] é [[2, 3, 4], [4, 6, 8], [8, 12, 16]]
    # o produto diádico só pode ser realizado se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None

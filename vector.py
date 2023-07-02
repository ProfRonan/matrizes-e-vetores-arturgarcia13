"""Módulo com as funções de manipulação de vetores."""
from tipos import Escalar, Matriz, Vetor


def norma(x: Vetor) -> Escalar | None:
    """Calcula a norma de um vetor"""
    if x == []:
        return None
    soma_quadrados = 0.0

    for ele in x:
        soma_quadrados += ele**2
    result = soma_quadrados ** (1 / 2)
    return result


def soma(x: Vetor, y: Vetor) -> Vetor | None:
    """Soma dois vetores"""
    if len(x) != len(y):
        return None
    if x == [] and y == []:
        return []

    result = [0 for _ in range(len(x))]

    for i, ele_x in enumerate(x):
        result[i] = ele_x + y[i]
    return result


def multiplicacao_por_escalar(vetor: Vetor, escalar: Escalar) -> Vetor:
    """Multiplica um vetor por um escalar"""
    vetor_res = [0] * len(vetor)

    for i, ele in enumerate(vetor):
        vetor_res[i] = ele * escalar
    return vetor_res


def produto_interno(x: Vetor, y: Vetor) -> Escalar | None:
    """Calcula o produto interno de dois vetores"""
    if len(x) != len(y):
        return None
    if x == [] and y == []:
        return 0

    result = int()

    for i, elex in enumerate(x):
        result += elex * y[i]
    return result


def produto_vetorial(x: Vetor, y: Vetor) -> Vetor | None:
    """Calcula o produto vetorial de dois vetores"""
    if len(x) != 3 or len(y) != 3:
        return None
    result = [0] * len(x)
    for i in range(3):
        result[i] = x[(i + 1) % 3] * y[(i + 2) % 3] - x[(i + 2) % 3] * y[(i + 1) % 3]

    return result


def produto_diadico(x: Vetor, y: Vetor) -> Matriz | None:
    """Calcula o produto diádico de dois vetores"""
    if len(x) != len(y):
        return None

    result = []

    for elex in x:
        linha = []
        for eley in y:
            linha.append(elex * eley)
        result.append(linha)

    return result

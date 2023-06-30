"""Módulo com as funções de manipulação de matrizes."""


def soma(x: list[list[float]], y: list[list[float]]) -> list[list[float]] or None:
    """
    Soma duas matrizes
    """
    # Testa se as duas matrizes possuem a mesma quantidade de linhas
    if len(x) != len(y):
        return None

    # Verifica se as duas matrizes possuem a mesma quantidade de colunas em cada linha
    for i, row_x in enumerate(x):
        if len(row_x) != len(y[i]):
            return None

    # Inicializa a matriz de resultado com zeros
    matriz_res = [[0] * len(x[0]) for n in range(len(x))]

    # Realiza a soma das matrizes
    for i, row_x in enumerate(x):
        for j, element_x in enumerate(row_x):
            matriz_res[i][j] = element_x + y[i][j]
    return matriz_res


def multiplicacao_por_escalar(
    matriz: list[list[float]], escalar: float
) -> list[list[float]]:
    """Multiplica uma matriz por um escalar"""
    # Cria uma matriz de reserva
    matriz2 = [[el for el in linha] for linha in matriz]
    # Multiplica cada termo da matriz pelo escalar
    for i, row in enumerate(matriz):
        for j, element in enumerate(row):
            matriz2[i][j] = element * escalar
    return matriz2


def multiplicacao(
    x: list[list[float]], y: list[list[float]]
) -> list[list[float]] | None:
    """Multiplica duas matrizes"""
    # Testa se a matriz x tem o mesmo numero de colunas da matriz y
    if len(x) == 0 or len(y) == 0 or len(x[0]) == 0 or len(y[0]) == 0:
        return []
    if len(x[0]) != len(y):
        return None

    # Matriz resultado
    matriz_res = [[0] * len(y[0]) for _ in range(len(x))]

    # Realiza a multiplicação
    # Para cada linha de x
    for i, row_x in enumerate(x):
      # Para cada coluna de y
        for j, col_y in enumerate(y[0]):
            # Para cada coluna de x
            for k, col_x in enumerate(x[0]):
                matriz_res[i][j] += x[i][k] * y[k][j]
    return matriz_res


def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    if len(x)== [] and len(x[0]) == []:
        return 0
    soma_quadrados = float()
    for linha in x:
        for ele in linha:
            soma_quadrados += ele**2
    sqr = soma_quadrados**(1/2)
    return sqr

def e_simetrica(x: list[list[float]]) -> bool:
    """Verifica se uma matriz é simétrica"""
    # TODO: implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta
    # Cria o modelo da matriz transposta
    matriz_trans = [[0] * len(x) for _ in range(len(x[0]))]
    # Transfere cada elemento do matriz original para seu lugar na transposta
    for i, row_x in enumerate(x):
        for j, element_x in enumerate(row_x):
            matriz_trans[j][i] = element_x
    for row_x in x:
        for row_trans in matriz_trans:
            for ele_x in row_x:
                for ele_y in row_trans:
                    if ele_x != ele_y:
                        return False
    return True



def transposta(x: list[list[float]]) -> list[list[float]]:
    """Calcula a transposta de uma matriz"""
    if x == [] :
        return []
    # Cria o modelo da matriz transposta
    matriz_trans = [[0] * len(x) for _ in range(len(x[0]))]
    # Transfere cada elemento do matriz original para seu lugar na transposta
    for i, row_x in enumerate(x):
        for j, element_x in enumerate(row_x):
            matriz_trans[j][i] = element_x
    return matriz_trans

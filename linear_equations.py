#Exercício 3
#3.2.1
def produto_interno(vetor_1,vetor_2):
    """
    tuplo,tuplo -> real
    calcula e devolve o produto interno de dois vetores representados pelo tuplos de entrada.
    """
    produto = 0
    for i in range(len(vetor_1)):
        produto += vetor_1[i]*vetor_2[i]
    return float(produto)

#3.2.2
def verifica_convergencia(matriz,constantes,soluçao,precisao):
    """
    tuplo,tuplo,tuplo,real -> booleano
    devolve False se o módulo do produto interno de cada linha da matriz (1º tuplo)
    com o vetor soluçao (3ºtuplo) menos o respetivo valor do vetor das constantes(2ºtuplo)
    for menor que o valor da precisao (valor real) e devolve True caso contrário.
    """
    for i in range(len(matriz)):
        if not abs(produto_interno(matriz[i],soluçao)-constantes[i])<precisao:
            return False
    return True

#3.2.3
def retira_zeros_diagonal(matriz,constantes):
    """
    tuplo,tuplo -> tuplo,tuplo
    a função vai reordenar as linhas da matriz(1ºtuplo) de forma a que os elementos nas diagonais da matriz
    não sejam nulos e fazer as mesmas mudanças no vetor das constantes(2ºtuplo).
    """
    matriz = list(matriz)
    constantes = list(constantes)
    for i in range(len(matriz)):
            for p in range(len(matriz)):
                if matriz[i][i] == 0 and matriz[p][i] != 0 and matriz[i][p]!=0:
                    matriz[p] , matriz[i] = matriz[i] , matriz[p]
                    constantes[p] , constantes[i] = constantes[i] , constantes[p]
                    break
    return ((tuple(matriz)),(tuple(constantes)))

#3.2.4
def eh_diagonal_dominante(matriz):
    """
    tuplo->booleano
    devolve True se a matriz(representada pelo tuplo) é diagonalmente dominante e False caso contrário.
    """
    soma_linha = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j:
                soma_linha += abs(matriz[i][j])
            else:
                diagonal = abs(matriz[i][i])
        if diagonal < soma_linha:
            return False
        soma_linha = 0
    return True

#3.2.5
def resolve_sistema(matriz,constantes,precisao):
    """
    tuplo,tuplo,real -> tuplo
    Sabendo que os elementos de entrada são respetivamente, uma matriz, um vetor de constantes um valor de precisão,
    a funçao devolve a soluçao do sistema de equações de entrada aplicando o método de Jacobi.
    """
    soluçao = []
    soluçao_anterior = []
    if not (type(matriz)==tuple and len(matriz)!=0 and type(constantes)==tuple and len(constantes)!=0\
        and len(constantes) == len(matriz) and type(precisao)==float and precisao>0):
        raise ValueError('resolve_sistema: argumentos invalidos')
    for i in range(len(matriz)):
        if not (type(matriz[i])==tuple and len(matriz)==len(matriz[i]) and isinstance(constantes[i],(int,float))):
            raise ValueError('resolve_sistema: argumentos invalidos')
        soluçao += [0]
        soluçao_anterior += [0]
        for j in range(len(matriz[i])):
            if not isinstance(matriz[i][j],(int,float)):
                raise ValueError('resolve_sistema: argumentos invalidos')
    matriz,constantes = retira_zeros_diagonal(matriz,constantes)
    if eh_diagonal_dominante(matriz) == False:
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    while verifica_convergencia(matriz,constantes,soluçao,precisao)==False:
        for i in range(len(matriz)):
            soluçao[i] += (constantes[i]-produto_interno(matriz[i],soluçao_anterior))/matriz[i][i]
            #aplicação do Método de Jacobi
        soluçao_anterior = soluçao.copy()
    return tuple(soluçao)

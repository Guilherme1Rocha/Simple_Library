#Exercício 2
#2.2.1
def calcula_quocientes(votos,deputados):
    """
    dicionário,inteiro -> dicionário
    calcula os quocientes através do Método de Hondt e devolve o dicionário cujas chaves correspodem aos 
    partidos e cujos valores correspodem a uma lista(de comprimento igual ao número de deputados)
    que contém os quocientes por ordem decrescente.
    """
    count = 1
    quocientes = []
    votos_copy = votos.copy()
    for key in votos_copy.keys():
        while count<=deputados:  #o tamanho da lista é igual ao número de deputados
            quocientes += [votos_copy[key]/count]
            count += 1
        votos_copy[key] = quocientes
        quocientes = []
        count = 1
    return votos_copy

#2.2.2
def atribui_mandatos(votos,deputados):
    """
    dicionário,inteiro -> lista
    devolve uma lista ordenada cujo comprimento é igual ao número de deputados e cujos elementos correspodem
    ao partido que obteve cada mandato.
    """
    mandatos = []
    votos_quocientes = (calcula_quocientes(votos,deputados))
    max = 0
    while len(mandatos)<deputados:
        for i in votos_quocientes.keys():
            if max<votos_quocientes[i][0]:
                partido = i
                max = votos_quocientes[i][0]
            if max == votos_quocientes[i][0]:
                if votos[partido]>votos[i]:
                    partido = i
                    max = votos_quocientes[i][0]
        mandatos += [partido]
        max = 0
        del votos_quocientes[partido][0]
    return mandatos

#2.2.3
def obtem_partidos(info):
    """
    dicionário -> lista
    devolve uma lista ordenada por ordem alfabética que contém todos os partidos presentes 
    em todos os círculos eleitorais
    """
    partidos = []
    for i in info.keys():
        for k in info[i]['votos'].keys():
            if k not in partidos:
                partidos.append(k)
    partidos = sorted(partidos)
    return partidos

#2.2.4
def obtem_resultado_eleicoes(info):
    """
    dicionário -> lista
    devolve uma lista cujos elementos são tuplos constituídos respetivamente pelo: partido,
    o número de deputados do partido e o número de votos do partido ordenada de forma decrescente
    tendo em conta o número de deputados ,e, no caso de serem iguais o número de votos.
    """
    soma_votos = 0
    if not (type(info)==dict and len(info)>0):
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    for i in info.keys():
        if not (type(info[i])==dict and len(info[i])==2):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        for j in info[i].keys():
            if not ((j == 'votos' or j =='deputados') and type(info[i]['votos']==dict)\
                and type(info[i]['deputados'])==int and info[i]['deputados']>0 ):
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        for j in info[i]['votos'].keys():
            if not (type(j)==str and type(info[i]['votos'][j])==int and info[i]['votos'][j]>=0):
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            soma_votos += info[i]['votos'][j]
        if soma_votos==0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        soma_votos = 0
    resultado = []
    lista_votos = []
    lista_mandatos = []
    partidos = obtem_partidos(info)
    count = 0
    for i in info.keys():
        t = info[i]['votos']
        for j in partidos:
            if j in t.keys():
                lista_votos.append((j,t[j]))
        deputados = info[i]['deputados']
        mandatos = atribui_mandatos(t,deputados)
        for i in partidos:
            for k in mandatos:
                if i==k:
                    count+=1
            lista_mandatos.append((i,count))
            count=0
    for partido in partidos:
        deputados = 0
        for i,j in lista_mandatos:
            if partido == i:
                deputados += j
        votos_partido = 0
        for i,j in lista_votos:
            if partido == i:
                votos_partido+=j
        resultado.append((partido,deputados,votos_partido))
    resultado.sort(key = lambda x:x[2],reverse=True)
    #ordena a lista tendo em conta as especificações
    return resultado
#Exercício 1
#1.2.1
def limpa_texto(cadeia):
    """
    cad.carateres -> cad.carateres
    a função irá substtuir os careteres brancos ASCII com espaços e
    retirar os espaços desnecessários na cad.carateres
    """
    white_c = '\n''\t''\f''\v''\r'
    for i in range(len(cadeia)):
        if cadeia[i] in white_c:
            cadeia = cadeia.replace(cadeia[i],' ')
    cadeia = ' '.join((cadeia.strip()).split())
    #juntar através de espaços a cad.carateres tranformada em lista 
    return cadeia

#1.2.2
def corta_texto(cadeia,largura):
    """
    cad.carateres,inteiro positivo -> cad.carateres,cad.carateres
    a função irá cortar a cad.carateres em duas partes, sendo que
    o comprimento da primeira parte tem de ser igual ao inteiro.
    """
    if len(cadeia) <= largura:
        cadeia_1 = cadeia
        cadeia_2 = ''
    if len(cadeia)>largura: 
        if cadeia[largura-1]==' ':
            cadeia_1,cadeia_2 = cadeia[:largura-1],cadeia[largura:]
            return cadeia_1,cadeia_2
        if cadeia[largura]==' ':
            cadeia_1, cadeia_2 = cadeia[:largura+1],cadeia[largura+1:]
            return cadeia_1,cadeia_2
        for i in range(largura-1,-1,-1):
            if cadeia[i] == ' ':
                break
            #encontrar o espaço mais próximo de forma a não cortar palavras.
        cadeia_1,cadeia_2 = cadeia[:i],cadeia[i+1:]
    return cadeia_1,cadeia_2

#1.2.3
def insere_espacos(cadeia,largura):
    """
    cad.carateres,inteiro -> cad.carateres
    retorna uma cad.carateres de comprimento igual ao inteiro com espaços entre palavras,
    se apresentar mais de uma palavra. No caso contrário adiciona espaços no final da cadeia.
    """
    count = 0 #corresponde ao número de espaços na cadeia
    espaços = largura - len(cadeia)
    for i in range(len(cadeia)):
        if cadeia[i] == ' ':
            count+=1
    if count == 0:
        cadeia_final = str(cadeia) + ' '*(largura-len(cadeia))
        return cadeia_final
    cadeia = cadeia.split(' ')
    while espaços!=0:
        for i in range(len(cadeia)-1):
            if espaços == 0:
                break
            cadeia[i] += ' '
            espaços-=1
    cadeia_final = ' '.join(cadeia)
    return cadeia_final

#1.2.4
def justifica_texto(cadeia,largura):
    """
    cad.carateres,inteiro -> tuplo
    devolve um tuplo de cadeias de carateres justificadas ou seja de comprimento igual à largura da coluna
    """
    if not (type(cadeia)==str and len(cadeia)>0 and type(largura)==int and largura>0):
        raise ValueError('justifica_texto: argumentos invalidos')
    cadeia = limpa_texto(cadeia)
    cadeia = cadeia.split(' ')
    for i in range(len(cadeia)):
        if not len(cadeia[i])<=largura:
            raise ValueError('justifica_texto: argumentos invalidos')
    cadeia = ' '.join(cadeia)
    if len(cadeia)<=largura:
        return ((corta_texto(cadeia,largura)[0]) + ' '*(largura-len(cadeia))),
    resultado = ((corta_texto(cadeia,largura)[0]),)
    texto = corta_texto(cadeia,largura)[1]
    while len(texto)>largura:
        resto = corta_texto(texto,largura)
        texto = resto[1]
        resultado += (resto[0],)
    resultado += (resto[1],)
    resultado_final = ()
    for i in range (len(resultado)-1):
        resultado_final += (insere_espacos(resultado[i],largura),)
    resultado_final += ((resto[1] + ' '*(largura-len(resto[1]))),)
    #o último elemento do tuplo deve apresentar espaços apenas no final
    return resultado_final
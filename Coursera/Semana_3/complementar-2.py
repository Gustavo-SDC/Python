# Desafio da Videoaula

'''

Dados: três números

Ação: aplicar os números na formula de baskara

Restrições: caso as haja duas raízes reais distindas, imprimir na ordem crescente.

Resultado: 
    Imprimir: "Esta equação não possui raízes reais", quando não houver raízes reais.
    Imprimir: "a raiz desta equação é X ", quando houver apenas uma raiz.
    Imprimir: "a raiz dupla desta equação é X", quando a raiz for dupla.
    Imprimir: "as raízes da equação são X e Y", onde X e Y são os valores das raízes.

'''

raiz_crescente = []

#Input de dados
a = float(input("Coloque o valor de A: "))
b = float(input("Coloque o valor de B: "))
c = float(input("Coloque o valor de C: "))

#Aplicação da Fórmula

delta = ( b ** 2 ) - 4 * a * c

if delta == 0:
    x1 = -b / 2 * a

    x1 = str(x1)
    print("a raiz desta equação é " +x1)

if delta < 0:
    print("esta equação não possui raízes reais")

if delta > 0:
    delta = delta ** 0.5
    div = 2 * a
    b = -b

    dd1 = b + delta
    dd2 = b - delta

    x1 = dd1 / div
    x2 = dd2 / div

    if x1 == x2:
        x1 = str(x1)
        print("a raiz dupla desta equação é " +x1)

    else:

        raiz_crescente.append(x1)
        raiz_crescente.append(x2)

        raiz_crescente.sort()

        r1 = raiz_crescente[0]
        r2 = raiz_crescente[1]
        r1 = str(r1)
        r2 = str(r2)

        print("as raízes da equação são " +r1+ " e " +r2 )

# Verificando Ordenação

'''

Dados: Três números.

Ação: Verificar se eles estão em ordem crescente ou não.

Restrições: Deve ser um número!!

Resultado: imprimir "Crescente" caso os números impultados formem uma P.A, ou imprimir "Não está em ordem crescente"

'''

lista = []

x = int(input("Coloque o primeiro número: "))
y = int(input("Coloque o segundo número: "))
z = int(input("Coloque o terceiro número: "))


lista.append(x + y + z)


if x < y < z:
    print("Crescente")

else:
    print("Não está em ordem crescente")
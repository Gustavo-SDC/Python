# FizzBuzz

'''

Dados: Número de entrada.

Ação: Descobrir se o número é divisível por 3 e por 5.

Restrições: Deve ser um número inteiro.

Resultado: imprimir o valor caso ele não seja divisível, e imprimir uma mensagem caso seja divisível.

'''


x = int(input("Digite um número: "))

if x % 5 == 0 and x % 3 == 0:
    print("FizzBuzz")

else:
    print(x)
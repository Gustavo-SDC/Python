# FizzBuzz

'''

Dados: Número inteiro

Ação: Dividir este número por 3

Restrições: O número deve ser inteiro

Resutado: Devo imprimir o número de entrada caso ele não seja divisível por três, e caso seja, devo imprimir qye
          ele é divisível.

'''

#Receber um valor

x = int(input("Coloque um número inteiro: "))

if x % 5 == 0:
    print("Buzz")

else:
    print(x)
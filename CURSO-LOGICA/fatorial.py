#Fatorial de um número


# Dados: número
# Oq fazer: Realizar o cálculo do fatorial e printar
# Restrições: Deve ser um número inteiro
# Resultado: Fatorial


#input do valor

x = int(input("Digite um valor: "))

if x > 0:
    fatorial = 1
    for item in range(1, x +1):
        fatorial = fatorial * item

    print(fatorial)
#Distância entre dois pontos

'''

Dados: receber 4 números, 2 números respectivos a um ponto e 2 a outro pronto, sendo x e y.

Ação: Calcular a distância entre estes dois pontos.

Restrições: Os números devem ser colocados na ordem correta, um de cada vez.

Resultado:
    imprimir: 'Longe' se a distância for MAIOR OU IGUAL a 10
    imprimir: 'Perto' se a distancia for MENOR que 10

'''

# Entrada de dados

x1 = float(input("Coloque a coordenada X do ponto 1: "))
y1 = float(input("Coloque a coordenada Y do ponto 1: "))
x2 = float(input("Coloque a coordenada X do ponto 2: "))
y2 = float(input("Coloque a coordenada Y do ponto 2: "))


# Processamento dos dados

dt = (((x1-x2)**2)+((y1+y2)**2))**(0.5)

if dt >= 10:
    print("Longe")

else:
    print("Perto")
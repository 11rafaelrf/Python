#Um algoritmo que exibe a tabuada de um número fornecido pelo usuário.
numero = int(input("Escolha Uma Tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

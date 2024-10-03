#Definição das funções
def Celsius_Fahrenheit(n1):
    return 9 * n1 / 5 + 32

def Celsius_Kelvin(n1):
    return n1 + 273.15

def Fahrenheit_Celsius(n1):
    return (n1 - 32) * 5/9

def Fahrenheit_Kelvin(n1):
    return (n1 - 32) / 1.8 + 273.15

def Kelvin_Celsius(n1):
    return n1 - 273.15
    
def Kelvin_Fahrenheit(n1):
    return (n1 - 273.15) * 1.8 + 32

#Função exibir menu
def exibirMenu():
    print("CALCULADORA DAS CONVEÇÕES:")
    print("Menu de escolha")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")
    print("0. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha

#Declaração de variáveis
opcao = 7
n1 = 0

while opcao != 0:
    opcao = exibirMenu()
    
    if opcao in [1, 2, 3, 4, 5, 6]:
        n1 = float(input("Insira o grau/valor escolhido: "))

    if opcao == 1:
        print(f"A Converção de Celsius para Fahrenheit é: {Celsius_Fahrenheit(n1)}\n")
    elif opcao == 2:
        print(f"A Converção de Celsius para Kelvin é: {Celsius_Kelvin(n1)}\n")
    elif opcao == 3:
        print(f"A Converção de Fahrenheit para Celsius é: {Fahrenheit_Celsius(n1)}\n")
    elif opcao == 4:
        print(f"A Converção de Fahrenheit para Kelvin é: {Fahrenheit_Kelvin(n1)}\n")
    elif opcao == 5:
        print(f"A Converção de Kelvin para Celsius é: {Kelvin_Celsius(n1)}\n") 
    elif opcao == 6:
        print(f"A Converção de Kelvin para Fahrenheit é: {Kelvin_Fahrenheit(n1)}\n") 
    elif opcao == 0:
        print("Saindo...")   
    else:
        print("Opção Inválida. Tente novamente.\n")
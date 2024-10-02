#Definição das funções
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Divisão por zero não é permitida."

def resto_divisao(n1, n2):
    if n2 != 0:
        return n1 % n2
    else:
        return "Erro: Divisão por zero não é permitida."

#Função exibir menu
def exibirMenu():
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS:")
    print("Menu de escolha")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha

#Declaração de variáveis
opcao = 0
n1 = 0
n2 = 0

while opcao != 6:
    opcao = exibirMenu()
    
    if opcao in [1, 2, 3, 4, 5]:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

    
    if opcao == 1:
       print(f"A soma dos valores é: {soma(n1, n2)}\n")

    elif opcao == 2:
       print(f"A subtração dos valores é: {subtracao(n1, n2)}\n")
    elif opcao == 3:
       print(f"A multiplicação dos valores é: {multiplicacao(n1, n2)}\n")
    elif opcao == 4:
       print(f"A divisão dos valores é: {divisao(n1, n2)}\n")
    elif opcao == 5:
       print(f"O resto da divisão dos valores é: {resto_divisao(n1, n2)}\n") 
    elif opcao == 6:
        print("Finalizando o código!")   
    else:
        print("Opção Inválida. Tente novamente.\n")
    
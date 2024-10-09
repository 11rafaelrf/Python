#Definição das funções
def cateto_oposto(hipo, ca):
    return hipo ** 2 - ca **2

def cateto_adjacente(hipo, co):
    return hipo ** 2 - co **2

def hipotenusa(co, ca):
    return co ** 2 + ca **2


#Função exibir menu
def menu():
    print("TRIGOTEC - CALCULADORA TRIGONOMÉTRICA:")
    print("Menu de Opções/Triângulo Retângulo")
    print("1. Teorema de Pitágoras")
    print("2. Seno")
    print("3. Cosseno")
    print("4. Tangente")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha

def menu_pitagoras():
    print("Menu de Opções Pitágoras")
    print("1. Descobrir cateto oposto.")
    print("2. Descobrir cateto adjacente.")
    print("3. Descobrir hipotenusa.")
    escolha = int(input("Escolha uma opção: "))
    return escolha

#Declaração de Variável
opção = 0
hipo = 0
co = 0
ca = 0

def teorema_pitagoras(escolha):
    if escolha == 1:
        print(f"O Cateto Oposto é: {cateto_oposto(hipo, ca)}\n")

    elif escolha == 2:
        print(f"O Cateto Adjacente é: {cateto_adjacente(hipo, co)}\n")

    elif escolha == 3:
        print(f"A Hipotenusa é: {hipotenusa(co, ca)}\n")


menu()
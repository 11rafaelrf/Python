import math

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

def teorema_pitagoras(escolha):
    if escolha == 1:
        # Descobrir cateto oposto
        cateto_adjacente = float(input("Informe o cateto adjacente: "))
        hipotenusa = float(input("Informe a hipotenusa: "))
        cateto_oposto = math.sqrt(hipotenusa**2 - cateto_adjacente**2)
        print(f"Cateto oposto: {cateto_oposto:.2f}")

    elif escolha == 2:
        # Descobrir cateto adjacente
        cateto_oposto = float(input("Informe o cateto oposto: "))
        hipotenusa = float(input("Informe a hipotenusa: "))
        cateto_adjacente = math.sqrt(hipotenusa**2 - cateto_oposto**2)
        print(f"Cateto adjacente: {cateto_adjacente:.2f}")

    elif escolha == 3:
        # Descobrir hipotenusa
        cateto_oposto = float(input("Informe o cateto oposto: "))
        cateto_adjacente = float(input("Informe o cateto adjacente: "))
        hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
        print(f"Hipotenusa: {hipotenusa:.2f}")

def calcular_seno():
    angulo = float(input("Informe o ângulo em graus: "))
    seno = math.sin(math.radians(angulo))
    print(f"Seno de {angulo}°: {seno:.2f}")

def calcular_cosseno():
    angulo = float(input("Informe o ângulo em graus: "))
    cosseno = math.cos(math.radians(angulo))
    print(f"Cosseno de {angulo}°: {cosseno:.2f}")

def calcular_tangente():
    angulo = float(input("Informe o ângulo em graus: "))
    tangente = math.tan(math.radians(angulo))
    print(f"Tangente de {angulo}°: {tangente:.2f}")

while True:
    escolha_principal = menu()

    if escolha_principal == 1:
        escolha_pitagoras = menu_pitagoras()
        teorema_pitagoras(escolha_pitagoras)

    elif escolha_principal == 2:
        calcular_seno()

    elif escolha_principal == 3:
        calcular_cosseno()

    elif escolha_principal == 4:
        calcular_tangente()

    elif escolha_principal == 5:
        print("Saindo...")
        break

    else:
        print("Opção inválida.")


while opcao != 5:
    opcao = Menu()
    
    if opcao in [1]:
        def Menu_Pitagoras():
          print("Menu de Opções Pitágoras")
          print("1. Descobrir cateto oposto.")
          print("2. Descobrir cateto adjacente.")
          print("3. Descobrir hipotenusa. ")
          escolha = int(input("Escolha uma opção: "))
          return escolha
        

    opcao = Menu()

    if opcao == 2:
        print(f"A Converção de Celsius para Kelvin é: {Celsius_Kelvin(n1)}\n")
    elif opcao == 3:
        print(f"A Converção de Fahrenheit para Celsius é: {Fahrenheit_Celsius(n1)}\n")
    elif opcao == 4:
        print(f"A Converção de Fahrenheit para Kelvin é: {Fahrenheit_Kelvin(n1)}\n")
    elif opcao == 5:
        print("Saindo...")   
    else:
        print("Opção Inválida. Tente novamente.\n")


    if opcao in [1, 2, 3, 4]:
        n1 = float(input("Insira o valor escolhido: "))
        n2 = float(input("Insira o valor escolhido: "))
        n3 = float(input("Insira o valor escolhido: "))

    if opcao == 1:
        print(f"O Teorema de Pitágoras é : {Celsius_Fahrenheit(n1)}\n")
    elif opcao == 2:
        print(f"A Converção de Celsius para Kelvin é: {Celsius_Kelvin(n1)}\n")
    elif opcao == 3:
        print(f"A Converção de Fahrenheit para Celsius é: {Fahrenheit_Celsius(n1)}\n")
    elif opcao == 4:
        print(f"A Converção de Fahrenheit para Kelvin é: {Fahrenheit_Kelvin(n1)}\n")
    elif opcao == 5:
        print("Saindo...")   
    else:
        print("Opção Inválida. Tente novamente.\n")
    
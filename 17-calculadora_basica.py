#Calculadora das operações básicas
opcao = 0
while opcao != 6:
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS: ")
    print("Menu de escolha")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")

    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
       num1 = float(input("Digite o primeiro número: "))
       num2 = float(input("Digite o segundo número: "))
       resultado = num1 + num2
       print(f"O resultado da soma é: {resultado}")

    elif opcao == 2:
       num1 = float(input("Digite o primeiro número: "))
       num2 = float(input("Digite o segundo número: "))
       resultado = num1 - num2
       print(f"O resultado da subtração é: {resultado}")

    elif opcao == 3:
       num1 = float(input("Digite o primeiro número: "))
       num2 = float(input("Digite o segundo número: "))
       resultado = num1 * num2
       print(f"O resultado da multiplicação é: {resultado}")

    elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")

    elif opcao == 5:
            num1 = float(input("Digite o dividendo: "))
            num2 = float(input("Digite o divisor: "))
            if num2 != 0:
                resultado = num1 % num2
                print(f"Resultado do resto da divisão: {resultado}")
            else:
                print("Erro: Divisor não pode ser zero.")
      
    elif opcao == 6:
        print("Saindo...")
        
    else:
        print("Opção Inválida")
    
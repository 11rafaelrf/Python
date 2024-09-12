# Função para calcular o IMC e fornecer a classificação
def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    
    # Determina a classificação
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 35:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return imc, classificacao

# Recebe o peso e a altura do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC e obtém a classificação
imc, classificacao = calcular_imc(peso, altura)

# Exibe o resultado do IMC e a classificação
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")

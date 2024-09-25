# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius / 5) + 32
    return fahrenheit

# Solicita ao usuário a temperatura em °C
try:
    temperatura_celsius = float(input("Digite a temperatura em °C: "))

    # Chama a função para converter
    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

    # Exibe o resultado
    print(f"A temperatura em °F é: {temperatura_fahrenheit:.2f}°F")
except ValueError:
    print("Por favor, insira um valor numérico válido.")

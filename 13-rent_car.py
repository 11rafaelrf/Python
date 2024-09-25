# Função para calcular o preço total
def calcular_preco(qtd_dias, km_percorridos):
    preco_por_dia = 60.00  # preço por dia
    preco_por_km = 0.15     # preço por Km
    custo_total = (qtd_dias * preco_por_dia) + (km_percorridos * preco_por_km)
    return custo_total

# Solicita ao usuário a quantidade de dias e Km percorridos
try:
    dias_alugados = int(input("Informe a quantidade de dias que o carro foi alugado: "))
    km_percorridos = float(input("Informe a quantidade de Km percorridos: "))

    # Chama a função para calcular o preço
    preco = calcular_preco(dias_alugados, km_percorridos)

    # Exibe o resultado
    print(f"O total a pagar pelo aluguel do carro é: R${preco:.2f}")
except ValueError:
    print("Por favor, insira valores válidos.")

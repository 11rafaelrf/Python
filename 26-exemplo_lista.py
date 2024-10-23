# Crie uma lista de 5 números inteiros fornecidos pelo usuário e imprima o maior,
# o menor e a soma de todos os elementos.
numero = [0,0,0,0,0]

for num in range(5):
    numero[num] = int(input(f"Digite o {num + 1}º número: "))

maior = max(numero)
menor = min(numero)
soma = sum(numero)


print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma dos números é: {soma}")

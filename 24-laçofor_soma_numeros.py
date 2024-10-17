#Um algoritmo que calcula a soma dos números pares entre 1 e 50.
soma = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma += i
print(f"A soma dos números pares entre 1 e 50 é: {soma}")

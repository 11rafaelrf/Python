numero = 0

while numero <= 100:
    numero += 1

    if numero == 6:
        print("Não vou mostrar o 6.")
        continue

    if 10 <= numero <= 27:
        print(f"Não vou mostrar o {numero}.")
        continue

    print(numero)

    if numero == 40:
        break


print("Acabou.")

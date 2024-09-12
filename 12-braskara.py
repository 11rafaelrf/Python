import math

# Função para calcular as raízes da equação do 2º grau
def calcular_raizes(a, b, c):
    # Calcula o discriminante
    delta = b**2 - 4*a*c
    
    # Verifica o valor do discriminante e calcula as raízes
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma única raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais:")
        print(f"Raiz 1: {raiz1:.2f}")
        print(f"Raiz 2: {raiz2:.2f}")

# Recebe os coeficientes A, B e C do usuário
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

# Verifica se A é diferente de zero (não é uma equação do 2º grau)
if a == 0:
    print("O coeficiente A não pode ser zero para uma equação do 2º grau.")
else:
    # Calcula e exibe as raízes
    calcular_raizes(a, b, c)

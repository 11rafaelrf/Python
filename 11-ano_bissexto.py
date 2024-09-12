# Função para verificar se um ano é bissexto
def verificar_bissexto(ano):
    # Verifica se o ano é divisível por 400, se sim, é bissexto
    if ano % 400 == 0:
        return True
    # Verifica se o ano é divisível por 100, se sim, não é bissexto
    elif ano % 100 == 0:
        return False
    # Verifica se o ano é divisível por 4, se sim, é bissexto
    elif ano % 4 == 0:
        return True
    # Se não satisfaz nenhuma das condições acima, não é bissexto
    else:
        return False

# Recebe o ano do usuário
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Verifica se o ano é bissexto e exibe o resultado
if verificar_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

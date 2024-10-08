# Código infinito com break
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')

    if nome == 'sair':
        break # para execução do while, sai do loop de repetição

    print(f'Seu nome é {nome}')

print('Acabou')

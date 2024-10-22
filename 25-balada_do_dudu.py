# balada com restirção de idade

print("\nBem Vindo a BALADA DO DUDU")
idade = int(input("Informe Sua Idade: "))

if idade >= 18:
    print("Pode Entrar... Bem Vindo!!!")

elif idade >=16:
    autorizacao = input("Seus Pais Autorização Sua Entrada? (SIM/NÃO)")
    if autorizacao == "SIM":
        print("Pode Entrar... Bem Vindo!!!")
    else:
        print("Não Pode Entrar... Até A Próxima!!!")

else:
    print("Menor de Idade... Não Pode Entrar!!!")

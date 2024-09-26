# Solicita ao usuário a quantidade de cigarros por dia e anos fumando
cigarros_por_dia = int(input("Quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Quantidade de anos fumando: "))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)
# Exibe o resultado
print(f"Redução do tempo de vida {redução_em_dias:.2f} dias de vida.")

import os

nome_arquivo_dvr = "0000000000000000-201118-000000-003000-01p402000000.mp4"
nome_arquivo, extensao = os.path.splitext(nome_arquivo_dvr)

nome_arquivo = nome_arquivo.split("-")

data = nome_arquivo[1]
hora = nome_arquivo[2]
milenio = "20"

nome_arquivo = milenio+data+hora+extensao 

print(nome_arquivo)
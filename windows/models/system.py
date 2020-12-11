import json

class System():

    def __init__(self):
        pass

    def ReadJson(self):
        arquivo = "C:/Users/Administrator/Documents/desenvolvimento/manipilacao_de_diretorio-main/manipilacao_de_diretorio-main/config.json"

        with open(arquivo, 'r') as json_file:
            dados = json.load(json_file)

            return dados

import json

class System():

    def __init__(self):
        pass

    def ReadJson(self):
        arquivo = "./config.json"

        with open(arquivo, 'r') as json_file:
            dados = json.load(json_file)

            return dados

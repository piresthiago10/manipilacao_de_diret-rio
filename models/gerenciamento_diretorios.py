import os
import shutil
from os.path import join

# exemplo de nome de arquivo 0000000000000000-201118-000000-003000-01p402000000
# --------------------------------------------data---hora-------------camera---


class GerenciamentoDiretorio():
    def __init__(self, diretorio_origem):
        self.diretorio_origem = diretorio_origem

    def get_carro(self):
        pass

    def get_data(self):
        pass

    def get_hora(self):
        pass

    def get_camera(self):
        pass

    def cria_diretorio(self, carro, camera, data, hora):
        path = join(carro, camera, data, hora)

        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        return path

    def renomeia_arquivo(self, nome_arquivo_dvr):

        nome_arquivo, extensao = os.path.splitext(nome_arquivo_dvr)

        nome_arquivo = nome_arquivo.split("-")

        data = nome_arquivo[1]
        hora = nome_arquivo[2]
        milenio = "20"

        nome_arquivo = milenio+data+hora+extensao

        return nome_arquivo

    def move_arquivo(self, diretorio_origem, diretorio_destino, arquivo):

        diretorio_destino = join(diretorio_destino, arquivo)
        shutil.move(diretorio_origem, diretorio_destino)
        
        return None

    def run(self):
        arquivos = os.listdir(self.diretorio_origem)

        for arquivo in arquivos:
            if arquivo.endswith(".mp4"):
                pass

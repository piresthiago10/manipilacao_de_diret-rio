import os
import shutil
from os.path import join

# exemplo de nome de arquivo 0000000000000000-201118-000000-003000-01p402000000
# --------------------------------------------data---hora-------------camera---
# root@srv-homologacao:~# ls /home/publico/imagens/50101/camera1/2020-11-10/20201110235959.mp4
# /home/publico/imagens/50101/camera1/2020-11-10/20201110235959.mp4
# root@srv-homologacao:~# ls /home/publico/imagens/50102/2020-11-10/recorder/3/0000000000000000-201118-000000-003000-01p402000000.mp4/

class GerenciamentoDiretorio():
    def __init__(self, diretorio_origem):
        self.diretorio_origem = diretorio_origem

    def get_infos(self):
        # recuperar carro, data, hora, camera 
        carro = None
        camera = None
        data = None
        hora = None
        return carro, camera, data, hora

    def cria_diretorio(self):
        carro, camera, data, hora = self.get_infos()
        path = join(carro, camera, data, hora)

        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        return path

    def renomeia_arquivo(self, nome_arquivo):

        nome_arquivo, extensao = os.path.splitext(nome_arquivo)

        nome_arquivo = nome_arquivo.split("-")

        data = nome_arquivo[1]
        hora = nome_arquivo[2]
        milenio = "20"

        novo_nome_arquivo = milenio+data+hora+extensao
        os.rename(nome_arquivo, novo_nome_arquivo)

        return novo_nome_arquivo

    def move_arquivo(self, diretorio_origem, diretorio_destino, novo_nome_arquivo):

        diretorio_origem = join(diretorio_origem, novo_nome_arquivo)
        diretorio_destino = join(diretorio_destino, novo_nome_arquivo)
        shutil.move(diretorio_origem, diretorio_destino)
        
        return None

    def run(self):
        arquivos = os.listdir(self.diretorio_origem)

        for arquivo in arquivos:
            if arquivo.endswith(".mp4"):
                pass

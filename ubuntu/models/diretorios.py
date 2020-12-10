import os
import shutil
from os.path import join

# exemplo de nome de arquivo 0000000000000000-201118-000000-003000-01p402000000.mp4
# --------------------------------------------data---hora-------------camera---
# root@srv-homologacao:~# ls /home/publico/imagens/50101/camera1/2020-11-10/20201110235959.mp4
# /home/publico/imagens/50101/camera1/2020-11-10/20201110235959.mp4
# root@srv-homologacao:~# ls /home/publico/imagens/50102/2020-11-10/recorder/3/0000000000000000-201118-000000-003000-01p402000000.mp4/


class GerenciamentoDiretorio():

    def __init__(self, diretorio_origem, nome_arquivo):
        self.diretorio_origem = diretorio_origem
        self.nome_arquivo = nome_arquivo

    def get_infos(self):
        
        diretorio_origem = self.diretorio_origem.split("/")

        
        antigo_nome_arquivo = self.nome_arquivo
        nome_arquivo_split = self.nome_arquivo.split("-")

        carro = diretorio_origem[4]
        camera = "camera" + nome_arquivo_split[4][5]
        data = "20" + nome_arquivo_split[1]
        hora = nome_arquivo_split[2]
        extensao = self.nome_arquivo[-4:]
        return carro, camera, data, hora, antigo_nome_arquivo, extensao

    def cria_diretorio(self, carro, camera, data):

        path = join(carro, camera, data)

        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)

        return path

    def renomeia_arquivo(self, data, hora, extensao, diretorio_origem, antigo_nome_arquivo):

        novo_nome_arquivo = data+hora+extensao
        antigo_nome_arquivo = antigo_nome_arquivo
        try:
            os.rename(diretorio_origem+antigo_nome_arquivo, diretorio_origem+novo_nome_arquivo)
        except:
            pass
        return novo_nome_arquivo

    def move_arquivo(self, diretorio_origem, diretorio_destino, antigo_nome_arquivo, novo_nome_arquivo):

        diretorio_origem = join(diretorio_origem, antigo_nome_arquivo)
        diretorio_destino = join(diretorio_destino, novo_nome_arquivo)
        shutil.move(diretorio_origem, diretorio_destino)

        return None

    def run(self):

        diretorio_origem = self.diretorio_origem

        carro, camera, data, hora, antigo_nome_arquivo, extensao = self.get_infos()
        diretorio_destino = self.cria_diretorio(carro, camera, data)
        novo_nome_arquivo = self.renomeia_arquivo(data, hora, extensao, diretorio_origem, antigo_nome_arquivo)
        self.move_arquivo(diretorio_origem, diretorio_destino, antigo_nome_arquivo, novo_nome_arquivo)

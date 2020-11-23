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

        diretorio_origem = self.diretorio_origem.split("/")

        nome_arquivo, extensao = os.path.splitext(diretorio_origem[8])
        antigo_nome_arquivo = nome_arquivo
        nome_arquivo = nome_arquivo.split("-")

        carro = diretorio_origem[4]
        camera = "camera" + nome_arquivo[4][5]
        data = "20" + nome_arquivo[1]
        hora = nome_arquivo[2]
        extensao = extensao
        nome_arquivo = antigo_nome_arquivo

        return carro, camera, data, hora, nome_arquivo, extensao

    def cria_diretorio(self, carro, camera, data):

        path = join(carro, camera, data)

        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)

        return path

    def renomeia_arquivo(self, data, hora, extensao, nome_arquivo):

        novo_nome_arquivo = data+hora+extensao
        nome_arquivo = nome_arquivo+extensao
        try:
            os.rename('home/publico/Video/17025/2020-11-19/record/1/'+nome_arquivo, 'home/publico/Video/17025/2020-11-19/record/1/'+novo_nome_arquivo)
        except:
            pass
        return novo_nome_arquivo

    def move_arquivo(self, diretorio_origem, diretorio_destino, novo_nome_arquivo):

        diretorio_origem = join('home/publico/Video/17025/2020-11-19/record/1/', novo_nome_arquivo)
        diretorio_destino = join(diretorio_destino, novo_nome_arquivo)
        shutil.move(diretorio_origem, diretorio_destino)

        return None

    def run(self):

        diretorio_origem = self.diretorio_origem
        # arquivos = os.listdir(diretorio_origem)

        # # for arquivo in arquivos:
        # if arquivo.endswith(".mp4"):
        carro, camera, data, hora, nome_arquivo, extensao = self.get_infos()
        diretorio_destino = self.cria_diretorio(carro, camera, data)
        novo_nome_arquivo = self.renomeia_arquivo(data, hora, extensao, nome_arquivo)
        self.move_arquivo(diretorio_origem, diretorio_destino, novo_nome_arquivo)

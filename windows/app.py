import os
import time
from os.path import join

from models import diretorios
from models import system

System = system.System()
ReadJson = System.ReadJson()

def main():

    diretorio = ReadJson['diretorio']
    destino = ReadJson['destino']
    extensao = ReadJson['extensao']

    while True:
        for raiz, caminhos, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                path = join(raiz, arquivo)
                if path.endswith(extensao):
                    print(f'Trabalhando com o arquivo: {arquivo}')
                    GerenciamentoDiretorio = diretorios.GerenciamentoDiretorio(raiz, destino, arquivo)
                    GerenciamentoDiretorio.run()
                    time.sleep(5)
                else:
                    print(f'Manipulando: {path}')
                    os.remove(path)
                    time.sleep(5)


if __name__ == '__main__':
    print('**************************************************')
    print('*                                                *')
    print('*           MANIPULADOR DE DIRETÓRIOS            *')
    print('*                                                *')
    print('**************************************************')
    main()

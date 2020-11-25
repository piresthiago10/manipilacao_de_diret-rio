import os
from os.path import join

from models import diretorios
from models import system

System = system.System()
ReadJson = System.ReadJson()
def main():

    diretorio = ReadJson['diretorio']
    extensao = ReadJson['extensao']

    for raiz, diretorios, arquivos in os.walk(diretorio):
        for arquivo in raiz:
            path = join(raiz, arquivo)
            if path.endswith(extensao): 
                GerenciamentoDiretorio = diretorios.GerenciamentoDiretorio(raiz, arquivo)
                GerenciamentoDiretorio.run()
            else:
                os.remove(path) 

if __name__ == '__main__':
    main()
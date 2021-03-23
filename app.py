# -*- coding: utf-8 -*-

import os
import time
from os.path import join
from models import diretorios
from models import system
import time
import sys

def pega_nome_processo_ffmpeg():
    r = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(r)):
        s = r[i]
        if 'ffmpeg' in r[i]:
            return r[i].split(' ')[0]
    
    return None

def mata_processo(nome_processo):
    os.system('taskkill /F /im {}'.format(nome_processo))

def main():

    System = system.System()
    ReadJson = System.ReadJson()
    
    diretorio_raiz = ReadJson['diretorio_raiz']
    diretorio_destino = ReadJson['diretorio_destino']
    extensoes = ReadJson['extensao']

    logger = System.logger()

    while True:
        # Entender e melhorar a busca pelos arquivos.
        for raiz, caminhos, arquivos in os.walk(diretorio_raiz):
            GerenciamentoDiretorio = diretorios.GerenciamentoDiretorio(raiz, diretorio_destino, logger)
            
            arquivos_para_remover = []

            if len(arquivos) > 0:
                
                inicio = time.time()

                for arquivo in arquivos:

                    logger.info(f'Manipulando: {arquivo}')
                    print((f'Manipulando: {arquivo}'))

                    path = join(raiz, arquivo)
                    extensao = arquivo.split(".")[-1]

                    if os.path.getsize(path) > 0 and System.compara_tempo(path) == True:
                        
                        if extensao in extensoes:
                            GerenciamentoDiretorio.run(arquivo)
                            arquivos_para_remover.append(path)
                        else:
                            arquivos_para_remover.append(path)
                    
                    else:
                        logger.debug(f'Arquivo sendo descarregado, ignorado. {arquivo}')
                        print(f'Arquivo sendo descarregado, ignorado. {arquivo}')
                        continue
                
                #Verifica se ha processos ffmpeg travados
                print(f'Verificando processos ffmpeg')
                time.sleep(5)
                nome_processo = pega_nome_processo_ffmpeg()
                while pega_nome_processo_ffmpeg() is not None:
                    mata_processo(nome_processo)
                    time.sleep(1)
                    
                while len(arquivos_para_remover) > 0:
                    for arquivo in arquivos_para_remover:
                        os.remove(arquivo)
                        logger.info(f'Removido.')
                        print(f'Removido: {arquivo}')
                        arquivos_para_remover.remove(arquivo)

                fim = time.time()
                print(f'Tempo de execução: {fim - inicio}')

if __name__ == '__main__':
    print('**************************************************************')
    print('*                                                            *')
    print('*            MANIPULADOR DE DIRETORIOS INICIADO              *')
    print('*                                                            *')
    print('**************************************************************')
    while True:
        try:
            main()
        except Exception as e:
            print(f'Erro: {e}')
            time.sleep(3)

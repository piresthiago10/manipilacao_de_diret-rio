import os
import shutil
import datetime
import subprocess
from os.path import join
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

class GerenciamentoDiretorio():

    def __init__(self, diretorio_origem, diretorio_destino, logger):
        self.diretorio_origem = diretorio_origem
        self.destino = diretorio_destino
        self.logger = logger

    def get_car(self):
        """
        Varre o nome do arquivo de vídeo e recupera o nome do carro
        """
        drive, path = os.path.splitdrive(self.diretorio_origem)
        
        folders = []
        
        while True:
            path, folder = os.path.split(path)
            
            if folder != "":
                folders.append(folder)
            elif path != "":
                folders.append(path)
                break

        folders.reverse()
        return folders[2]

    @staticmethod
    def formata_data(data):
        FMT = "%y%m%d"
        data_completa = datetime.datetime.strptime(data, FMT)
        data_formatada = data_completa.strftime("%Y-%m-%d")

        return data_formatada

    def get_file_infos(self, arquivo):
        
        nome_arquivo_split = arquivo.split("-")
        camera = "camera" + nome_arquivo_split[4][5]
        data = nome_arquivo_split[1]
        hora = nome_arquivo_split[2]
        extensao = arquivo[-4:]

        return camera, data, hora, extensao

    def cria_diretorio(self, carro, camera, data):
        """
        Cria diretorio para armazenar os videos com nomes modificados
        """
        path = os.path.join(self.destino, carro, camera, data)
          
        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)

        return path

    @staticmethod
    def __converter_segundos(seconds):
        hours = seconds // 3600
        seconds %= 3600
        mins = seconds // 60
        seconds %= 60
        return hours, mins, seconds

    def __get_video_duration(self, path_arquivo):
        
        video = VideoFileClip(path_arquivo)
        video_duration = int(video.duration)
        hours, mins, secs = self.__converter_segundos(video_duration)
        video.close()
        
        return hours, mins, secs


    def cortar_video_por_minuto(self, arquivo, diretorio_destino):
        
        hours, mins, secs = self.__get_video_duration(os.path.join(self.diretorio_origem, arquivo))
        video_duration = 60 * hours + mins
        
        input_file = os.path.join(self.diretorio_origem, arquivo)

        camera, data, hora, extensao = self.get_file_infos(arquivo)
        
        FMT = "%y%m%d%H%M%S"

        # Hora Inicial do Arquivo
        time = datetime.datetime.strptime(data+hora, FMT)

        lista_novos_arquivos = []

        for x in range(video_duration):
            
            t1 = x * 60
            t2 = t1 + 60

            target_file = os.path.join(diretorio_destino, time.strftime("%Y%m%d%H%M%S") + extensao)

            if os.path.isfile(target_file):
                self.logger.warning(f'Existe: {target_file}')
                print(f'Existe: {target_file}')
                continue

            tempo_inicio_convertido = datetime.timedelta(seconds = t1)
            tempo_inicio_formatado = datetime.datetime.strptime(str(tempo_inicio_convertido), "%H:%M:%S").time()

            tempo_fim_convertido = datetime.timedelta(seconds = t2)
            tempo_fim_formatado = datetime.datetime.strptime(str(tempo_fim_convertido), "%H:%M:%S").time()

            cmnd = ['ffmpeg', '-i', input_file, '-b:v', '64k', '-bufsize', '64k', '-ss', str(tempo_inicio_formatado), '-to', str(tempo_fim_formatado), '-c', 'copy', target_file]
            p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err =  p.communicate()
            self.logger.info(f'Fragmento criado: {target_file}')
            print(f'Fragmento criado: {target_file}')

            lista_novos_arquivos.append(target_file)
            # Adiciona 1 minuto ao nome do arquivo
            time = time + datetime.timedelta(seconds=60)
        
        return lista_novos_arquivos

    def converte_avi_para_mp4(self, arquivo_avi):

        input_file = os.path.join(self.diretorio_origem, arquivo_avi)
        file_renamed = arquivo_avi.split('.avi')[0] + '.mp4'
        output_file = os.path.join(self.diretorio_origem, file_renamed)

        clip = VideoFileClip(input_file)
        clip.write_videofile(output_file, audio=False)
        clip.close()

        return file_renamed

    def run(self, arquivo):

        carro = self.get_car()
        camera, data, hora, extensao = self.get_file_infos(arquivo)

        diretorio_destino = self.cria_diretorio(carro, camera, self.formata_data(data))

        novos_arquivos = self.cortar_video_por_minuto(arquivo, diretorio_destino)

        if 'avi' in extensao:
            for arquivo in novos_arquivos:
                self.converte_avi_para_mp4(arquivo)
                os.remove(arquivo)
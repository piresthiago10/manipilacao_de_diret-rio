# -*- coding: utf-8 -*-

import datetime
import json
import logging
import logging.config
import os
from datetime import datetime, timedelta


class System():

    def __init__(self):
        pass

        self._source_path = os.path.split(
            os.path.dirname(os.path.realpath(__file__)))[0]

        self._config_folder = os.path.join(self._source_path, 'config')
        if not os.path.isdir(self._config_folder):
            os.makedirs(self._config_folder)

        self._log_folder = os.path.join(self._source_path, 'logs')
        if not os.path.isdir(self._log_folder):
            os.makedirs(self._log_folder)

    def ReadJson(self):
        """
        Lê o arquivo com as configurações do manipulador de arquivos de vídeos e diretórios.
        """
        config_file = 'config.json'
        arquivo = os.path.join(self._config_folder, config_file)

        with open(arquivo, 'r') as json_file:
            dados = json.load(json_file)

            return dados

    def get_nome_log(self):
    
        date_time = datetime.now()
        str_date_time = date_time.strftime("%d-%m-%Y") + ".log"
        log_file_folder = os.path.join(self._log_folder, str_date_time)
        # if not os.path.isdir(self._log_folder):
        #     os.makedirs(self._log_folder)

        return log_file_folder

    def logger(self):

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

        nome_arquivo_log = self.get_nome_log()
        file_handler = logging.FileHandler(nome_arquivo_log)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    def compara_tempo(self, path):
        tempo_arquivo = os.path.getatime(path)
        diferenca_tempo = datetime.now() - datetime.fromtimestamp(tempo_arquivo)
        json_data = self.ReadJson()
        tempo_comparacao = json_data["tempo_comparacao"]
        datetime_diferenca_tempo = diferenca_tempo.total_seconds()
        
        if datetime_diferenca_tempo > tempo_comparacao:
            return True
        else:
            return False

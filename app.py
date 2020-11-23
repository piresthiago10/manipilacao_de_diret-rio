from models import diretorios
import os

diretorio_origem = "./home/publico/Video/17025/2020-11-19/record/1/17025-201119-030000-033000-01p402000000.mp4"


GerenciamentoDiretorio = diretorios.GerenciamentoDiretorio(diretorio_origem)

GerenciamentoDiretorio.run()
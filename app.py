from models import diretorios
import os
from os.path import join

dir = "home/publico/Video"
for root, dirs, files in os.walk(dir):
    for filename in files:
        path = join(root, filename)
        if path.endswith(".mp4"): 
            print(path)
            GerenciamentoDiretorio = diretorios.GerenciamentoDiretorio(root, filename)
            GerenciamentoDiretorio.run()
        else:
            os.remove(path) 
        #     # os.remove(dir)
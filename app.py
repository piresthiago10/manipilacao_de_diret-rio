from models import diretorios

diretorio_origem = "."
GerenciamentoDiretorio = diretorios.GerenciamentoDiretorio(diretorio_origem)
while True:
    GerenciamentoDiretorio.run()

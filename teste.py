from tkinter import Tk
from tkinter.filedialog import askopenfilename

janela_padrao = Tk().withdraw()
caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos de texto", "*.csv"), ("Arquivos csv", "*.csv")))

if caminho_do_arquivo:
    with open(caminho_do_arquivo, encoding='latin_1') as arquivo:
        for linha in arquivo:
            print(linha, end='')
else:
    print("Nenhum arquivo selecionado")
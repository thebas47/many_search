import os, sys
import tkinter as tk
from tkinter import filedialog


# Destinado a mensagens e interfaces no terminal
class CliInterfaces:

    def logo():
        print(r"""Many Searcher ©
=         =             
= =     = =    =   =    = =   =
=  =   =  =   = =  = =  =   =
=   = =   =  =   = =  = =   =
                                    Montana Software ™
        """)

    def salute(user):
        print(f"\nSeja bem vindo ao Many Searcher © {user}!")

    def catalogue():
        print(r"""
Qual busca pretende fazer?
1 - Busca Unitária de CNPJ
2 - CNPJ em Lote (Por planilha)
exit - Para Sair do Programa
        """)

class GuiInterfaces:

    @staticmethod
    def file_selector():
        try:
            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.askopenfilename(
                    title = "Selecione a planilha",
                    filetypes = [("Excel sheets", "*.xlsx"),]
                    )

            if not file_path:
                print("Nenhum arquivo foi selecionado.")
                return None

            if not os.path.isfile(file_path):
                print("O arquivo selecionado não é válido")
                return None

            print(f"Planilha selecionada: {file_path}")
            return file_path

        except Exception as e:
            print(f"Erro selecionando arquivo: {e}, file=sys.stderr")
            return None













            r

import os, sys
import tkinter as tk
from tkinter import filedialog

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

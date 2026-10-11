from searcher import CnpjSearcher
from sheets import ExcelProcessor
from interfaces import CliInterfaces as msg
from interfaces import GuiInterfaces as gui
import time

msg.logo()
time.sleep(1)

msg.salute("Usuario")
time.sleep(1)


def main():
    while True:

        msg.catalogue()
        operation = input(">>> ")

        match operation:
            case '1':
                cnpj = input("Digite o CNPJ ou 'exit' para sair da busca unitária\n>>> ")
                if cnpj.lower() == "exit":
                    break

                client = CnpjSearcher.search_cnpj(cnpj)
                print(client)

            case '2':
                file_path = gui.file_selector()
                if file_path:
                    sheet = ExcelProcessor(file_path)
                    sheet.process()
                    print("Processo terminado!")
                else:
                    print("Algo deu errado no processo")

            case 'exit':
                print("Saindo do programa...")
                break

if __name__ == "__main__":
    main()

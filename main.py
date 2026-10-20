from services.cnpj_searcher import CnpjSearcher
from services.cep_searcher import CepSearcher
from workers.excel_work import ExcelProcessor
from interfaces.cli_interface import CliInterfaces as msg
from interfaces.gui_interface import GuiInterfaces as gui
import time

def main():
    msg.logo()
    time.sleep(1)

    msg.salute("Usuário")
    time.sleep(1)

    while True:

        msg.catalogue()
        operation = input(">>> ")

        match operation:
            case '1':
                cnpj = msg.unit_cnpj()
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


            case '3':
                cep = msg.unit_cep()
                if cep.lower() == 'exit':
                    break

                address = CepSearcher.search_cep(cep)
                print(address)

            case 'exit':
                print("Saindo do programa...")
                break

if __name__ == "__main__":
    main()

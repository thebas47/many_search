from openpyxl import load_workbook
import time
from datetime import datetime
from api.cnpj.base_cnpj_api import BaseCnpjApiError
from api.cnpj.api_cnpj_factory import ApiCnpjFactory
from cleaners.cnpj import CnpjCleaner

class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process(self):
        workbook = load_workbook(self.file_path)
        worksheet = workbook.active

        for row in range(2, worksheet.max_row + 1):
            cnpj = worksheet.cell(row=row, column=1).value

            if not cnpj:
                continue

            self._process_row(worksheet, row, cnpj)

        workbook.save(self.file_path)

    def _process_row(self, worksheet, row, cnpj):
        cnpj = CnpjCleaner.normalize(cnpj)

        if not CnpjCleaner.is_valid(cnpj):
            worksheet.cell(row=row, column=2).value = "CNPJ inválido"
            print(f"O CNPJ {cnpj} é inválido ou contém um erro de digitação.")
            return
        
        providers = ApiCnpjFactory.get_providers()
        for attempt, provider in enumerate(providers, start=1):
            try:
                time.sleep(0.2)
                client = provider.search(cnpj)

                if client is None:
                    print(f"O {attempt}° provedor não retornou dados para o CNPJ {cnpj}"i)
                    continue
                self._write_client(worksheet, row, client)
                return

            except BaseCnpjApiError as error:
                print(f"Falha no {attempt}° provedor")
                continue

        worksheet.cell(row=row, column=2).value = "Erro na Consulta"
        print(f"Nenhum provedor encontrou dados para o CNPJ {cnpj}.")

    @staticmethod
    def _write_client(worksheet, row, client):
        worksheet.cell(row=row, column=1).value = client.cnpj
        worksheet.cell(row=row, column=2).value = client.razao
        worksheet.cell(row=row, column=3).value = client.rua
        worksheet.cell(row=row, column=4).value = client.num
        worksheet.cell(row=row, column=5).value = client.bairro
        worksheet.cell(row=row, column=6).value = client.municipio
        worksheet.cell(row=row, column=7).value = client.estado
        worksheet.cell(row=row, column=8).value = client.cep
        worksheet.cell(row=row, column=9).value = client.email
        worksheet.cell(row=row, column=10).value = client.fone
        worksheet.cell(row=row, column=11).value = client.fonte
        print(f"\nÚltima atualização: {datetime.now()}\nÚltimo CNPJ processado: {client.razao}\n")

from api import CnpjApi, CnpjApiError
from parser import CnpjaParser
from cnpj import CnpjCleaner
from sheets import ExcelProcessor

class CnpjSearcher:

    @staticmethod
    def search_cnpj(cnpj):

        cnpj = CnpjCleaner.normalize(cnpj)

        if not CnpjCleaner.is_valid(cnpj):
            print("CNPJ Invalido")
            return

        try:
            data = CnpjApi.get_company(cnpj)

        except CnpjApiError:
            print("Não foi possível consultar a API")
            return

        return CnpjaParser.parse(data)

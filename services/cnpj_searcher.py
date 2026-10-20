from api.cnpja_api import CnpjaApi, CnpjaApiError
from parsers.cnpj.cnpja_parser import CnpjaParser
from cleaners.cnpj import CnpjCleaner

class CnpjSearcher:

    @staticmethod
    def search_cnpj(cnpj):

        cnpj = CnpjCleaner.normalize(cnpj)

        if not CnpjCleaner.is_valid(cnpj):
            print("CNPJ Invalido")
            return

        try:
            data = CnpjaApi.get_company(cnpj)

        except CnpjaApiError:
            print("Não foi possível consultar a API")
            return

        return CnpjaParser.parse(data)

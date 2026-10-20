from api.viacep_api import ViacepApi, ViacepApiError
from parsers.cep.viacep_parser import ViacepParser
from cleaners.cep import CepCleaner

class CepSearcher:

    @staticmethod
    def search_cep(cep):

        cep = CepCleaner.normalize(cep)

        if not CepCleaner.is_valid(cep):
            print("CEP Invalido")
            return

        try:
            data = ViacepApi.get_cep(cep)

        except ViacepApiError:
            print("Não foi possível consultar a API")
            return

        return ViacepParser.parse(data)

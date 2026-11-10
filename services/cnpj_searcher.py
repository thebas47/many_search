from api.cnpj.base_cnpj_api import BaseCnpjApiError
from api.cnpj.api_cnpj_factory import ApiCnpjFactory
from cleaners.cnpj import CnpjCleaner

class CnpjSearcher:

    @staticmethod
    def search_cnpj(cnpj):

        cnpj = CnpjCleaner.normalize(cnpj)

        if not CnpjCleaner.is_valid(cnpj):
            print("CNPJ Invalido")
            return
        
        providers = ApiCnpjFactory.get_providers()
        attempts = 0
        for provider in providers:

            try:
                client = provider.search(cnpj)

                if client:
                    return client

            except BaseCnpjApiError as error:
                attempts += 1
                print(f"Falha no {attempts}° provedor, Trocando provedor...\n")
                continue

        print("\nNenhuma API Conseguiu consultar o CNPJ")
        return None

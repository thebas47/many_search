import requests

from api.cnpj.base_cnpj_api import BaseCnpjApi, BaseCnpjApiError

class CnpjaApiError(BaseCnpjApiError):
    pass

class CnpjaApi(BaseCnpjApi):

    @staticmethod
    def get_company(self, cnpj: str) -> dict:
        base_url = f"https://open.cnpja.com/office/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise CnpjaApiError from error
        
        except requests.exceptions.RequestException as error:
            raise CnpjaApiError from error

import requests

from api.cnpj.base_cnpj_api import BaseCnpjApi, BaseCnpjApiError

class CnpjWsApiError(BaseCnpjApiError):
    pass

class CnpjWsApi(BaseCnpjApi):

    def get_company(self, cnpj: str) -> dict:
        base_url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise CnpjWsApiError from error
        
        except requests.exceptions.RequestException as error:
            raise CnpjWsApiError from error

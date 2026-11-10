import requests

from api.cnpj.base_cnpj_api import BaseCnpjApi, BaseCnpjApiError

class BrasilApiError(BaseCnpjApiError):
    pass

class BrasilApi(BaseCnpjApi):

    def get_company(self, cnpj: str) -> dict:
        base_url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise BrasilApiError from error
        
        except requests.exceptions.RequestException as error:
            raise BrasilApiError from error
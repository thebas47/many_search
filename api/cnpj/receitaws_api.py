import requests

from api.cnpj.base_cnpj_api import BaseCnpjApi, BaseCnpjApiError

class ReceitaWsApiError(BaseCnpjApiError):
    pass

class ReceitaWsApi(BaseCnpjApi):

    def get_company(self, cnpj: str) -> dict:
        base_url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise ReceitaWsApiError from error
        
        except requests.exceptions.RequestException as error:
            raise ReceitaWsApiError from error
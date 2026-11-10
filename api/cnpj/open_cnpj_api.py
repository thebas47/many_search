import requests

from api.cnpj.base_cnpj_api import BaseCnpjApi, BaseCnpjApiError

class OpenCnpjApiError(BaseCnpjApiError):
    pass

class OpenCnpjApi(BaseCnpjApi):

    def get_company(self, cnpj: str) -> dict:
        base_url = f"https://api.opencnpj.org/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise OpenCnpjApiError from error
        
        except requests.exceptions.RequestException as error:
            raise OpenCnpjApiError from error
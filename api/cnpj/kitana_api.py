import requests

from api.cnpj.base_cnpj_api import BaseCnpjApi, BaseCnpjApiError

class KitanaApiError(BaseCnpjApiError):
    pass

class KitanaApi(BaseCnpjApi):

    def get_company(self, cnpj: str) -> dict:
        base_url = f"https://kitana.opencnpj.com/cnpj/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise KitanaApiError from error
        
        except requests.exceptions.RequestException as error:
            raise KitanaApiError from error
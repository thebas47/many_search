import requests

class CnpjApiError(Exception):
    pass

class CnpjApi:

    @staticmethod
    def get_company(cnpj):
        base_url = f"https://open.cnpja.com/office/{cnpj}"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise CnpjApiError from error
        
        except requests.exceptions.RequestException as error:
            raise CnpjApiError from error
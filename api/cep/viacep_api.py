import requests

class ViacepApiError(Exception):
    pass

class ViacepApi:

    @staticmethod
    def get_cep(cep):
        base_url = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.JSONDecodeError as error:
            raise ViacepApiError from error
        
        except requests.exceptions.RequestException as error:
            raise ViacepApiError from error

from abc import ABC, abstractmethod

class BaseCnpjApiError(Exception):
    pass

class BaseCnpjApi(ABC):

    @abstractmethod
    def get_company(self, cnpj: str) -> dict:
        """
        Consulta dados de cnpj na api
        """
        pass
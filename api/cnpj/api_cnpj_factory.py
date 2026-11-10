from api.cnpj.cnpja_api import CnpjaApi
from api.cnpj.receitaws_api import ReceitaWsApi
from api.cnpj.cnpj_ws_api import CnpjWsApi
from api.cnpj.kitana_api import KitanaApi
from api.cnpj.open_cnpj_api import OpenCnpjApi
from api.cnpj.brasil_api import BrasilApi

from parsers.cnpj.cnpja_parser import CnpjaParser
from parsers.cnpj.receitaws_parser import ReceitaWsParser
from parsers.cnpj.cnpjws_parser import CnpjWsParser
from parsers.cnpj.kitana_parser import KitanaParser
from parsers.cnpj.open_cnpj_parser import OpenCnpjParser
from parsers.cnpj.brasilapi_parser import BrasilApiParser

from services.cnpj_provider import CnpjProvider

class ApiCnpjFactory:

    @staticmethod
    def get_providers():
        return [
            CnpjProvider(CnpjaApi(), CnpjaParser),
            CnpjProvider(ReceitaWsApi(), ReceitaWsParser),
            CnpjProvider(BrasilApi(), BrasilApiParser),
            CnpjProvider(CnpjWsApi(), CnpjWsParser),
            CnpjProvider(KitanaApi(), KitanaParser),
            CnpjProvider(OpenCnpjApi(), OpenCnpjParser),
        ]

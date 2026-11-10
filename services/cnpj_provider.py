class CnpjProvider:

    def __init__(self, api, parser):
        self.api = api
        self.parser = parser

    def search(self, cnpj):

        data = self.api.get_company(cnpj)

        return self.parser.parse(data)
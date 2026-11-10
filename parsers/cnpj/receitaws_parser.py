from model.client import Client

class ReceitaWsParser:

    @staticmethod
    def parse(data):

        return Client(
            cnpj=data.get("cnpj", ""),
            razao=data.get("nome", "Não Informado"),
            rua=data.get("logradouro", "Não Informado"),
            num=data.get("numero", "Não Informado"),
            bairro=data.get("bairro", "Não Informado"),
            municipio=data.get("municipio", "Não Informado"),
            estado=data.get("uf", "Não Informado"),
            cep=data.get("cep", "Não Informado"),
            email=data.get("email", "Não Informado"),
            fone=data.get("telefone", "Não informado"),
            fonte="RECEITA WS API"
        )

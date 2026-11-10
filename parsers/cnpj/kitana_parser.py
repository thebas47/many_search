from model.client import Client

class KitanaParser:

    @staticmethod
    def parse(data):

        establishment = data.get("data") or {}

        return Client(
            cnpj=establishment.get("cnpj") or "Não Informado",
            razao=establishment.get("razaoSocial") or "Não Informado",
            rua=establishment.get("logradouro") or "Não Informado",
            num=establishment.get("numero") or "Não Informado",
            bairro=establishment.get("bairro") or "Não Informado",
            municipio=establishment.get("municipio") or "Não Informado",
            estado=establishment.get("uf") or "Não Informado",
            cep=establishment.get("cep") or "Não Informado",
            email=establishment.get("email") or "Não Informado",
            fone=establishment.get("telefone") or "Não Informado",
            fonte="KITANA API"
        )

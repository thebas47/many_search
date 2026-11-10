from model.client import Client

class BrasilApiParser:

    @staticmethod
    def parse(data):

        return Client(
            cnpj=data.get("cnpj") or "Não Informado",
            razao=data.get("razao_social") or "Não Informado",
            rua=(data.get("descricao_tipo_de_logradouro") or "") + " " + (data.get("logradouro") or ""),
            num=data.get("numero") or "Não Informado",
            bairro=data.get("bairro") or "Não Informado",
            municipio=data.get("municipio") or "Não Informado",
            estado=data.get("uf") or "Não Informado",
            cep=data.get("cep") or "Não Informado",
            email=data.get("email") or "Não Informado",
            fone =data.get("ddd_telefone_1") or "Não Informado",
            fonte="BRASIL API"
        )

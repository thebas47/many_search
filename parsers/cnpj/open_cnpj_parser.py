from model.client import Client

class OpenCnpjParser:

    @staticmethod
    def parse(data):

        phones = data.get("telefones") or [{}]

        return Client(
            cnpj=data.get("cnpj") or "Não Informado",
            razao=data.get("razao_social") or "Não Informado",
            rua=(data.get("tipo_logradouro") or "") + " " + (data.get("logradouro") or ""),
            num=data.get("numero") or "Não Informado",
            bairro=data.get("bairro") or "Não Informado",
            municipio=data.get("municipio") or "Não Informado",
            estado=data.get("uf") or "Não Informado",
            cep=data.get("cep") or "Não Informado",
            email=data.get("email") or "Não Informado",
            fone = ((phones[0].get("ddd") or "") +(phones[0].get("numero") or "")) or "Não Informado",
            fonte="OPEN CNPJ API"
        )

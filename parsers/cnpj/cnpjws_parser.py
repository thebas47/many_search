from model.client import Client

class CnpjWsParser:

    @staticmethod
    def parse(data):

        establishment = data.get("estabelecimento") or {}
        address = establishment.get("cidade") or {}
        state = establishment.get("estado") or {}

        return Client(
            cnpj=establishment.get("cnpj") or "Não Informado",
            razao=data.get("razao_social") or "Não Informado",
            rua=(establishment.get("tipo_logradouro") or "") + " " + (establishment.get("logradouro") or ""),
            num=establishment.get("numero") or "Não Informado",
            bairro=establishment.get("bairro") or "Não Informado",
            municipio=address.get("nome") or "Não Informado",
            estado=state.get("sigla") or "Não Informado",
            cep=establishment.get("cep") or "Não Informado",
            email=establishment.get("email") or "Não Informado",
            fone=(establishment.get("ddd1") or "") + (establishment.get("telefone1") or "") or "Não Informado",
            fonte="CNPJ WS API"
        )

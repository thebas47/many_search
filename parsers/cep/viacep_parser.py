from model.address import Address

class ViacepParser:

    @staticmethod
    def parse(data):

        return Address(
                rua=data.get("logradouro", "Não Informado"),
                complemento=data.get("complemento", "Não Informado"),
                unidade=data.get("unidade", "Não Informado"),
                bairro=data.get("bairro", "Não Informado"),
                localidade=data.get("localidade", "Não Informado"),
                uf=data.get("uf", "Não Informado"),
                estado=data.get("estado", "Não Informado"),
                regiao=data.get("regiao", "Não Informado"),
                ibge=data.get("ibge", "Não Informado"),
                gia=data.get("gia", "Não Informado"),
                ddd=data.get("ddd", "Não Informado"),
                siafi=data.get("siafi", "Não Informado"),
            )

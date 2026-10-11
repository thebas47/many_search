from model.client import Client

class CnpjaParser:

    @staticmethod
    def parse(data):
        address = data.get("address", {})
        company = data.get("company", {})
        email = (data.get("emails") or [{}])[0]
        phone = (data.get("phones") or [{}])[0]

        #email = emails[0] if emails else {}
        #phone = phones[0] if phones else {}

        return Client(
            cnpj=data.get("taxId", ""),
            razao=company.get("name", "Não Informado"),
            rua=address.get("street", "Não Informado"),
            num=address.get("number", "Não Informado"),
            bairro=address.get("district", "Não Informado"),
            municipio=address.get("city", "Não Informado"),
            estado=address.get("state", "Não Informado"),
            cep=address.get("zip", "Não Informado"),
            email=email.get("address", "Não Informado"),
            fone=phone.get("area", "") + phone.get("number", ""),
        )
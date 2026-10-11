from dataclasses import dataclass

@dataclass
class Client:
    cnpj: str
    razao: str
    rua: str
    num: str
    bairro: str
    municipio: str
    estado: str
    cep: str
    email: str
    fone: str

    def __str__(self):
        return(
            f"\nCNPJ: {self.cnpj}\n"
            f"Razão social: {self.razao}\n"
            f"Endereço: {self.rua}\n"
            f"Numero: {self.num}\n"
            f"Bairro: {self.bairro}\n"
            f"Município: {self.municipio}\n"
            f"Estado: {self.estado}\n"
            f"CEP: {self.cep}\n"
            f"E-mail: {self.email}\n"
            f"Telefone: {self.fone}\n"
        )
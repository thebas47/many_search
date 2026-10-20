from dataclasses import dataclass

@dataclass
class Address:
    rua: str
    complemento: str
    unidade: str
    bairro: str
    localidade: str
    uf: str
    estado: str
    regiao: str
    ibge: str
    gia: str
    ddd: str
    siafi: str

    def __str__(self):
        return(
            f"\nRua: {self.rua}\n"
            f"Complemento: {self.complemento}\n"
            f"Unidade: {self.unidade}\n"
            f"Bairro: {self.bairro}\n"
            f"Localidade: {self.localidade}\n"
            f"UF: {self.uf}\n"
            f"Estado: {self.estado}\n"
            f"Regiao: {self.regiao}\n"
            f"IBGE: {self.ibge}\n"
            f"GIA: {self.gia}\n"
            f"DDD: {self.ddd}\n"
            f"SIAFI: {self.siafi}\n"
        )

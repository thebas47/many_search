import re

class CnpjCleaner:

    @staticmethod
    def normalize(cnpj):
        cnpj = re.sub(r'\D', '',str(cnpj))
        return cnpj

    @staticmethod
    def is_valid(cnpj):
        if cnpj ==  "":
            return False
        elif len(cnpj) != 14:
            return False
        return True
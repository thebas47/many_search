import re

class CepCleaner:

    @staticmethod
    def normalize(cep):
        cep = re.sub(r'\D', '',str(cep))
        return cep

    @staticmethod
    def is_valid(cep):
        if cep ==  "":
            return False
        elif len(cep) != 8:
            return False
        return True

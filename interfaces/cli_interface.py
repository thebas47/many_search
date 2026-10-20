# Destinado a mensagens e interfaces no terminal
class CliInterfaces:

    def logo():
        print(r"""Many Searcher ©
=         =             
= =     = =    =   =    = =   =
=  =   =  =   = =  = =  =   =
=   = =   =  =   = =  = =   =
                                    Montana Software ™
        """)

    def salute(user):
        print(f"\nSeja bem vindo ao Many Searcher © {user}!")

    def catalogue():
        print(r"""
Qual busca pretende fazer?
1 - Busca Unitária de CNPJ
2 - CNPJ em Lote (Por planilha)
3 - Busca Unitária de CEP
exit - Para Sair do Programa
        """)

    def unit_cnpj():
        cnpj = input("Digite o CNPJ ou 'exit' para sair da busca unitária\n>>> ")
        return cnpj

    def unit_cep():
        cep = input("Digite o CEP ou 'exit' para sair da busca unitária\n>>> ")
        return cep

# Destinado a mensagens e interfaces
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
exit - Para Sair do Programa
        """)

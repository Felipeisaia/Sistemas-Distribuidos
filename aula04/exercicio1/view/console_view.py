class ConsoleView:
    """VIEW - unica parte do programa que imprime na tela.

    Model e Controller nunca chamam print(): quem mostra os dados e a View.
    """

    def titulo(self, texto):
        print()
        print(texto)

    def caixa_iniciou(self, nome):
        print(f"{nome} iniciou as vendas...")

    def deposito_realizado(self, nome, valor, saldo):
        print(f"{nome} alterou o saldo em {valor} e ficou {saldo}")

    def caixa_terminou(self, nome, fichas, valor_ficha):
        print(f"{nome} vendeu {fichas} fichas de R$ {valor_ficha:.2f}")

    def saldo_final(self, saldo, esperado):
        print()
        print(f"Saldo final apos vendas de fichas: R$ {saldo:.2f}")
        print(f"Saldo esperado                   : R$ {esperado:.2f}")
        if saldo == esperado:
            print("OK - o Lock garantiu a consistencia do saldo.")
        else:
            print(f"ERRO - diferenca de R$ {esperado - saldo:.2f} (condicao de corrida).")

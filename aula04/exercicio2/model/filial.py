import random


class Filial:
    """MODEL - uma filial com a SUA propria lista de vendas.

    Nao existe memoria compartilhada entre as filiais: cada thread mexe
    apenas no seu objeto Filial. Por isso nao ha secao critica e nao e
    preciso Lock. O resultado da soma fica guardado em self.total, que a
    thread principal le depois do join().
    """

    def __init__(self, nome, quantidade_registros):
        """Construtor

        Args:
            nome (str): identificacao da filial (ex: "Filial 1")
            quantidade_registros (int): quantos registros de venda gerar
        """
        self.nome = nome
        self.vendas = [random.randint(1, 1000) for _ in range(quantidade_registros)]
        self.total = 0

    def calcular_total(self):
        """Soma todas as vendas da filial e guarda o resultado no objeto

        Returns:
            int: o faturamento total desta filial
        """
        soma = 0
        for venda in self.vendas:  # soma local, so com os dados deste objeto
            soma += venda
        self.total = soma
        return self.total

    def quantidade_registros(self):
        """Quantidade de registros de venda da filial

        Returns:
            int: tamanho da lista de vendas
        """
        return len(self.vendas)

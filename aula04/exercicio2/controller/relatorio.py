import threading


class Relatorio:
    """CONTROLLER - operacoes que as threads executam sobre uma Filial.

    O Controller nao guarda os dados (isso e do Model) e nao imprime
    (isso e da View): ele so coordena os dois.
    """

    @staticmethod
    def processar(filial, view):
        """Metodo de classe que calcula o faturamento de uma filial

        A thread so enxerga a filial que recebeu como argumento: nao acessa
        variavel global nem a lista das outras filiais. O resultado fica
        guardado no atributo filial.total e e lido pela thread principal
        depois do join().

        Args:
            filial (Filial): objeto exclusivo desta thread
            view (ConsoleView): responsavel por mostrar os dados na tela
        """
        nome = threading.current_thread().name
        view.filial_iniciou(nome, filial.quantidade_registros())

        total = filial.calcular_total()

        view.filial_terminou(nome, total)

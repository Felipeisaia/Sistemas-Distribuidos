import threading
import time


class Operacao:
    """CONTROLLER - operacoes que as threads executam sobre a Conta.

    O Controller nao guarda o saldo (isso e do Model) e nao imprime
    (isso e da View): ele so coordena os dois.
    """

    @staticmethod
    def vender(conta, view, total_fichas, valor_ficha, detalhado=False, pausa=0.0):
        """Metodo de classe que realiza a venda de fichas

        Args:
            conta (Conta): objeto conta compartilhado entre os caixas
            view (ConsoleView): responsavel por mostrar os dados na tela
            total_fichas (int): quantidade de fichas a serem vendidas
            valor_ficha (int): valor unitario da ficha
            detalhado (bool): se True, mostra cada deposito na tela
            pausa (float): segundos de espera entre uma venda e outra;
                serve para forcar a troca de contexto e deixar o
                intercalamento das threads visivel na demonstracao
        """
        nome = threading.current_thread().name
        view.caixa_iniciou(nome)

        for _ in range(total_fichas):
            saldo = conta.depositar(valor_ficha)
            if detalhado:
                view.deposito_realizado(nome, valor_ficha, saldo)
            if pausa:
                time.sleep(pausa)

        view.caixa_terminou(nome, total_fichas, valor_ficha)

import threading


class Conta:
    """MODEL - conta com saldo_central e sincronizacao de acesso.

    Este objeto e compartilhado pelas 5 threads (os caixas), entao o
    saldo_central e a SECAO CRITICA e o acesso e protegido por um Lock.
    """

    def __init__(self, saldo):
        """Construtor

        Args:
            saldo (int): um objeto conta pode iniciar com saldo definido
        """
        self.saldo_central = saldo
        self.lock = threading.Lock()

    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta

        Args:
            valor (int): valor a ser adicionado ao saldo da conta

        Returns:
            int: o novo saldo, ja atualizado
        """
        with self.lock:  # exclusao mutua
            self.saldo_central += valor
            return self.saldo_central

    def consultar(self):
        """Retorna o saldo da conta

        Returns:
            int: saldo temporario da conta
        """
        with self.lock:  # exclusao mutua
            return self.saldo_central

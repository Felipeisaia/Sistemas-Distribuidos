import secrets
import time


class Token:

    VALIDADE_SEGUNDOS = 60

    def __init__(self):
        self.chave = secrets.token_hex(8).upper()
        self.criado_em = time.monotonic()

    def segundos_restantes(self):
        decorrido = time.monotonic() - self.criado_em
        return max(0, int(self.VALIDADE_SEGUNDOS - decorrido))

    def valido(self):
        return time.monotonic() - self.criado_em < self.VALIDADE_SEGUNDOS

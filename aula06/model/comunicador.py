import json
import socket
import threading


class Comunicador:
    """Encapsula o socket UDP. As mensagens trafegam como JSON em UTF-8."""

    TAMANHO_BUFFER = 4096

    def __init__(self, host="0.0.0.0", porta=0, timeout=None):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, porta))
        self.socket.settimeout(timeout)
        self.trava = threading.Lock()

    def enviar(self, mensagem, endereco):
        dados = json.dumps(mensagem).encode("utf-8")
        self.socket.sendto(dados, endereco)

    def receber(self):
        dados, endereco = self.socket.recvfrom(self.TAMANHO_BUFFER)
        return json.loads(dados.decode("utf-8")), endereco

    def requisitar(self, mensagem, endereco):
        """Envia e aguarda a resposta. A trava evita que duas requisicoes misturem respostas."""
        with self.trava:
            self.enviar(mensagem, endereco)
            resposta, _ = self.receber()
            return resposta

    def fechar(self):
        self.socket.close()

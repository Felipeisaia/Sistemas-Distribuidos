from datetime import datetime


class ServidorView:

    def _log(self, texto):
        print(f"[{datetime.now():%H:%M:%S}] {texto}")

    def iniciado(self, endereco):
        print()
        print("SERVIDOR UDP - CADASTRO E TOKEN")
        self._log(f"Escutando em {endereco[0]}:{endereco[1]} (Ctrl+C para encerrar)")

    def requisicao(self, endereco, mensagem):
        self._log(f"<- {endereco[0]}:{endereco[1]} {mensagem}")

    def resposta(self, endereco, resposta):
        self._log(f"-> {endereco[0]}:{endereco[1]} {resposta}")

    def pessoas(self, pessoas):
        self._log(f"Usuarios cadastrados ({len(pessoas)}):")
        for pessoa in pessoas:
            print(f"    - {pessoa}")

    def encerrado(self):
        self._log("Servidor encerrado.")

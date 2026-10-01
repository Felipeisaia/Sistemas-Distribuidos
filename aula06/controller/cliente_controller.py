import queue
import threading

from model.comunicador import Comunicador


class ClienteController:

    INTERVALO_TOKEN_MS = 10_000

    def __init__(self, host_servidor, porta_servidor, view):
        self.servidor = (host_servidor, porta_servidor)
        self.comunicador = Comunicador(timeout=3)
        self.view = view
        self.email = None
        self.respostas = queue.Queue()

        self.view.ao_cadastrar(self.cadastrar)
        self.view.ao_fechar(self.fechar)
        self.view.agendar(100, self.processar_respostas)

    def iniciar(self):
        self.view.executar()

    def cadastrar(self, nome, email):
        if not nome.strip() or not email.strip():
            self.view.erro("Informe nome completo e e-mail.")
            return
        mensagem = {"acao": "cadastrar", "nome": nome, "email": email}
        self.requisitar_em_segundo_plano(
            mensagem, lambda resposta: self.tratar_cadastro(resposta, email))

    def solicitar_token(self):
        mensagem = {"acao": "token", "email": self.email}
        self.requisitar_em_segundo_plano(mensagem, self.tratar_token)
        self.view.agendar(self.INTERVALO_TOKEN_MS, self.solicitar_token)

    def requisitar_em_segundo_plano(self, mensagem, ao_responder):
        # A requisicao roda fora da thread da GUI para a janela nao travar esperando o UDP.
        def tarefa():
            try:
                resposta = self.comunicador.requisitar(mensagem, self.servidor)
            except (TimeoutError, ConnectionResetError):
                resposta = {"status": "erro", "mensagem": "Servidor nao respondeu."}
            self.respostas.put((ao_responder, resposta))

        threading.Thread(target=tarefa, daemon=True).start()

    def processar_respostas(self):
        # O Tkinter so pode ser atualizado pela thread principal, por isso a fila.
        while not self.respostas.empty():
            ao_responder, resposta = self.respostas.get()
            ao_responder(resposta)
        self.view.agendar(100, self.processar_respostas)

    def tratar_cadastro(self, resposta, email):
        if resposta["status"] != "ok":
            self.view.erro(resposta["mensagem"])
            return
        self.view.sucesso(resposta["mensagem"])
        self.view.cadastro_concluido()
        self.email = email.strip().lower()
        self.solicitar_token()

    def tratar_token(self, resposta):
        if resposta["status"] != "ok":
            self.view.erro(resposta["mensagem"])
            return
        self.view.mostrar_token(resposta["token"], resposta["expira_em"], resposta["novo"])

    def fechar(self):
        self.comunicador.fechar()

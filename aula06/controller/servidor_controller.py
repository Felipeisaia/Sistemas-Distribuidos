import json

from model.cadastro import Cadastro
from model.comunicador import Comunicador


class ServidorController:

    def __init__(self, host, porta, view):
        self.comunicador = Comunicador(host, porta, timeout=1)
        self.cadastro = Cadastro()
        self.view = view
        self.acoes = {
            "cadastrar": self.cadastrar,
            "token": self.token,
        }

    def executar(self):
        self.view.iniciado(self.comunicador.socket.getsockname())
        try:
            while True:
                try:
                    mensagem, endereco = self.comunicador.receber()
                except TimeoutError:
                    # O timeout so serve para o Ctrl+C ser atendido no Windows.
                    continue
                except (json.JSONDecodeError, UnicodeDecodeError, ConnectionResetError):
                    # ConnectionResetError: no Windows o UDP acusa cliente que ja fechou.
                    continue

                self.view.requisicao(endereco, mensagem)
                acao = self.acoes.get(mensagem.get("acao"), self.desconhecida)
                resposta = acao(mensagem)
                self.comunicador.enviar(resposta, endereco)
                self.view.resposta(endereco, resposta)
        except KeyboardInterrupt:
            self.view.encerrado()
        finally:
            self.comunicador.fechar()

    def cadastrar(self, mensagem):
        nome = str(mensagem.get("nome", "")).strip()
        email = str(mensagem.get("email", "")).strip()

        if not nome or "@" not in email:
            return {"status": "erro", "mensagem": "Nome e e-mail validos sao obrigatorios."}

        pessoa = self.cadastro.cadastrar(nome, email)
        if pessoa is None:
            return {"status": "erro", "mensagem": f"E-mail {email} ja cadastrado."}

        self.view.pessoas(self.cadastro.pessoas)
        return {"status": "ok", "mensagem": f"{pessoa.nome} cadastrado com sucesso."}

    def token(self, mensagem):
        pessoa = self.cadastro.buscar(str(mensagem.get("email", "")))
        if pessoa is None:
            return {"status": "erro", "mensagem": "Usuario nao cadastrado."}

        token, novo = self.cadastro.obter_token(pessoa)
        return {
            "status": "ok",
            "token": token.chave,
            "novo": novo,
            "expira_em": token.segundos_restantes(),
        }

    def desconhecida(self, mensagem):
        return {"status": "erro", "mensagem": f"Acao desconhecida: {mensagem.get('acao')}"}

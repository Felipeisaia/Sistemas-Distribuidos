from model.pessoa import Pessoa
from model.token import Token


class Cadastro:

    def __init__(self):
        self.pessoas = []
        self.tokens = {}

    def buscar(self, email):
        email = email.strip().lower()
        for pessoa in self.pessoas:
            if pessoa.email == email:
                return pessoa
        return None

    def cadastrar(self, nome, email):
        pessoa = Pessoa(nome, email)
        if pessoa in self.pessoas:
            return None
        self.pessoas.append(pessoa)
        return pessoa

    def obter_token(self, pessoa):
        """Retorna (token, novo). Mantem o mesmo token enquanto estiver dentro dos 60s."""
        token = self.tokens.get(pessoa.email)
        if token is not None and token.valido():
            return token, False

        token = Token()
        self.tokens[pessoa.email] = token
        return token, True

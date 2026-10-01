class Pessoa:

    def __init__(self, nome, email):
        self.nome = nome.strip()
        self.email = email.strip().lower()

    def __eq__(self, outra):
        return isinstance(outra, Pessoa) and self.email == outra.email

    def __str__(self):
        return f"{self.nome} <{self.email}>"

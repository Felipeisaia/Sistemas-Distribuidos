class ResumoParcial:

    def __init__(self, numero_pedaco, trabalhador):
        self.numero_pedaco = numero_pedaco
        self.trabalhador = trabalhador
        self.linhas_lidas = 0
        self.contagem_por_codigo = {}

    def contabilizar(self, codigo):
        self.linhas_lidas += 1
        self.contagem_por_codigo[codigo] = self.contagem_por_codigo.get(codigo, 0) + 1

    def total_erros(self):
        return sum(self.contagem_por_codigo.values())


class ResumoFinal:

    def __init__(self):
        self.pedacos_processados = 0
        self.linhas_lidas = 0
        self.contagem_por_codigo = {}

    def juntar(self, resumo_parcial):
        self.pedacos_processados += 1
        self.linhas_lidas += resumo_parcial.linhas_lidas
        for codigo, quantidade in resumo_parcial.contagem_por_codigo.items():
            self.contagem_por_codigo[codigo] = (
                self.contagem_por_codigo.get(codigo, 0) + quantidade
            )

    def total_erros(self):
        return sum(self.contagem_por_codigo.values())

import multiprocessing

from model.pedaco import Pedaco
from model.resumo import ResumoFinal
from controller.trabalhador import Trabalhador


class Coordenador:

    def __init__(self, caminho_arquivo, quantidade_trabalhadores, linhas_por_pedaco, view):
        self.caminho_arquivo = caminho_arquivo
        self.quantidade_trabalhadores = quantidade_trabalhadores
        self.linhas_por_pedaco = linhas_por_pedaco
        self.view = view

    def dividir_arquivo(self):
        numero = 0
        linhas = []

        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linhas.append(linha)

                if len(linhas) == self.linhas_por_pedaco:
                    numero += 1
                    yield Pedaco(numero, linhas)
                    linhas = []

        if linhas:
            numero += 1
            yield Pedaco(numero, linhas)

    def executar(self):
        fila_tarefas = multiprocessing.Queue()
        fila_resultados = multiprocessing.Queue()

        trabalhadores = [
            multiprocessing.Process(
                target=Trabalhador.processar,
                args=(fila_tarefas, fila_resultados),
                name=f"Trabalhador {i + 1}",
            )
            for i in range(self.quantidade_trabalhadores)
        ]

        for trabalhador in trabalhadores:
            trabalhador.start()

        total_pedacos = 0
        for pedaco in self.dividir_arquivo():
            fila_tarefas.put(pedaco)
            total_pedacos += 1
            self.view.pedaco_enviado(pedaco.numero, pedaco.quantidade_linhas())

        for _ in trabalhadores:
            fila_tarefas.put(Trabalhador.SENTINELA)

        resumo_final = ResumoFinal()
        for _ in range(total_pedacos):
            resumo_parcial = fila_resultados.get()
            self.view.resumo_parcial(resumo_parcial)
            resumo_final.juntar(resumo_parcial)

        for trabalhador in trabalhadores:
            trabalhador.join()

        self.view.resultado_final(resumo_final)
        return resumo_final

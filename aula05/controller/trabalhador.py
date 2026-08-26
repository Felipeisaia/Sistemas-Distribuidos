import multiprocessing

from model.resumo import ResumoParcial


class Trabalhador:

    SENTINELA = None

    @staticmethod
    def processar(fila_tarefas, fila_resultados):
        nome = multiprocessing.current_process().name

        while True:
            pedaco = fila_tarefas.get()

            if pedaco is Trabalhador.SENTINELA:
                break

            resumo = Trabalhador.contar_erros(pedaco, nome)
            fila_resultados.put(resumo)

    @staticmethod
    def contar_erros(pedaco, nome):
        resumo = ResumoParcial(pedaco.numero, nome)

        for linha in pedaco.linhas:
            campos = linha.strip().split(",")
            if len(campos) == 4:
                resumo.contabilizar(campos[2])

        return resumo

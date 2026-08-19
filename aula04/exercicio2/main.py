import threading

from model.filial import Filial
from view.console_view import ConsoleView
from controller.relatorio import Relatorio

QTD_FILIAIS = 4
REGISTROS_POR_FILIAL = 10000


if __name__ == "__main__":
    view = ConsoleView()
    view.titulo("EXERCICIO 2 - FATURAMENTO POR FILIAL")

    # 4 listas independentes, uma por filial
    filiais = [
        Filial(f"Filial {i + 1}", REGISTROS_POR_FILIAL)
        for i in range(QTD_FILIAIS)
    ]

    threads = [
        threading.Thread(
            target=Relatorio.processar,
            args=(filial, view),
            name=filial.nome,
        )
        for filial in filiais
    ]

    for thread in threads:  # FORK dispara as 4 threads
        thread.start()
    for thread in threads:  # JOIN espera todas terminarem
        thread.join()

    # so a thread principal junta os resultados, depois do join()
    totais = [(filial.nome, filial.total) for filial in filiais]
    total_geral = sum(total for _, total in totais)
    view.faturamento_total(totais, total_geral)

import os
import multiprocessing

from view.console_view import ConsoleView
from controller.coordenador import Coordenador

ARQUIVO_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "erro.log")
QTD_TRABALHADORES = 4
LINHAS_POR_PEDACO = 25


if __name__ == "__main__":
    multiprocessing.freeze_support()

    view = ConsoleView()
    view.titulo("ANALISADOR DE LOGS DISTRIBUIDO - MAPREDUCE LOCAL")
    view.inicio(ARQUIVO_LOG, QTD_TRABALHADORES, LINHAS_POR_PEDACO)

    coordenador = Coordenador(
        ARQUIVO_LOG,
        QTD_TRABALHADORES,
        LINHAS_POR_PEDACO,
        view,
    )
    coordenador.executar()

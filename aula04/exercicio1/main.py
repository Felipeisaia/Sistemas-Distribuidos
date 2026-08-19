"""EXERCICIO 1 - Sistema de Caixa Centralizado de Evento.

Modulo 1: COM compartilhamento de memoria.
Os 5 caixas escrevem no mesmo saldo_central, entao existe secao critica
e o acesso e protegido por threading.Lock (exclusao mutua).

Execucao:  python main.py
"""

import threading

from model.conta import Conta
from view.console_view import ConsoleView
from controller.operacao import Operacao

QTD_CAIXAS = 5
FICHAS_POR_CAIXA = 1000
VALOR_FICHA = 10

# True mostra cada deposito na tela (bom para ver o intercalamento das
# threads, mas com 1.000 fichas por caixa sao 5.000 linhas)
DETALHADO = False

# Segundos de espera entre uma venda e outra. Com 0 a execucao e imediata;.
PAUSA = 0.0


if __name__ == "__main__":
    view = ConsoleView()
    view.titulo("EXERCICIO 1 - CAIXA CENTRALIZADO DO EVENTO")

    conta = Conta(0)  # Model COMPARTILHADO pelos 5 caixas

    caixas = [
        threading.Thread(
            target=Operacao.vender,
            args=(conta, view, FICHAS_POR_CAIXA, VALOR_FICHA, DETALHADO, PAUSA),
            name=f"Caixa {i + 1}",
        )
        for i in range(QTD_CAIXAS)
    ]

    for caixa in caixas:  # dispara as 5 threads
        caixa.start()
    for caixa in caixas:  # espera todas terminarem
        caixa.join()

    esperado = QTD_CAIXAS * FICHAS_POR_CAIXA * VALOR_FICHA
    view.saldo_final(conta.consultar(), esperado)

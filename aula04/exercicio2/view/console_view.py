class ConsoleView:

    def titulo(self, texto):
        print()
        print(texto)

    def filial_iniciou(self, nome, registros):
        print(f"{nome} somando {registros} registros...")

    def filial_terminou(self, nome, total):
        print(f"{nome} calculou o total local de R$ {total:.2f}")

    def faturamento_total(self, totais, total_geral):
        print()
        for nome, total in totais:
            print(f"  {nome:<10} R$ {total:>12.2f}")
        print("  " + "-" * 26)
        print(f"  {'TOTAL':<10} R$ {total_geral:>12.2f}")

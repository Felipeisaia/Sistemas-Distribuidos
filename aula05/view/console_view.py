class ConsoleView:

    def titulo(self, texto):
        print()
        print(texto)

    def inicio(self, arquivo, trabalhadores, linhas_por_pedaco):
        print(f"Arquivo: {arquivo}")
        print(f"Pool de {trabalhadores} trabalhadores, {linhas_por_pedaco} linhas por pedaco")
        print()

    def pedaco_enviado(self, numero, linhas):
        print(f"Coordenador enviou o pedaco {numero} ({linhas} linhas) para a fila")

    def resumo_parcial(self, resumo):
        codigos = ", ".join(
            f"{codigo}={quantidade}"
            for codigo, quantidade in sorted(resumo.contagem_por_codigo.items())
        )
        print(
            f"{resumo.trabalhador} devolveu o resumo do pedaco {resumo.numero_pedaco}: "
            f"{resumo.total_erros()} erros [{codigos}]"
        )

    def resultado_final(self, resumo):
        print()
        print("RESULTADO FINAL")
        print(f"  Pedacos processados: {resumo.pedacos_processados}")
        print(f"  Linhas lidas.......: {resumo.linhas_lidas}")
        print()
        print("  Erros por codigo:")
        for codigo, quantidade in sorted(resumo.contagem_por_codigo.items()):
            print(f"    codigo {codigo}: {quantidade}")
        print("  " + "-" * 22)
        print(f"    TOTAL DE ERROS: {resumo.total_erros()}")

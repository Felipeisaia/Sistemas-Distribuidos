import tkinter as tk
from tkinter import ttk


class ClienteView:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cliente UDP")
        self.root.resizable(False, False)
        self.segundos = 0
        self.contagem_id = None

        quadro = ttk.Frame(self.root, padding=16)
        quadro.grid()

        ttk.Label(quadro, text="Cadastro", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))

        ttk.Label(quadro, text="Nome completo:").grid(row=1, column=0, sticky="w")
        self.campo_nome = ttk.Entry(quadro, width=36)
        self.campo_nome.grid(row=1, column=1, pady=2)

        ttk.Label(quadro, text="E-mail:").grid(row=2, column=0, sticky="w")
        self.campo_email = ttk.Entry(quadro, width=36)
        self.campo_email.grid(row=2, column=1, pady=2)

        self.botao_cadastrar = ttk.Button(quadro, text="Cadastrar")
        self.botao_cadastrar.grid(row=3, column=1, sticky="e", pady=8)

        ttk.Separator(quadro).grid(row=4, column=0, columnspan=2, sticky="ew", pady=8)

        ttk.Label(quadro, text="Token", font=("Segoe UI", 12, "bold")).grid(
            row=5, column=0, columnspan=2, sticky="w")
        self.rotulo_token = ttk.Label(quadro, text="-", font=("Consolas", 16, "bold"))
        self.rotulo_token.grid(row=6, column=0, columnspan=2, pady=4)
        self.rotulo_validade = ttk.Label(quadro, text="Cadastre-se para receber um token.")
        self.rotulo_validade.grid(row=7, column=0, columnspan=2)

        self.rotulo_status = ttk.Label(quadro, text="", wraplength=320)
        self.rotulo_status.grid(row=8, column=0, columnspan=2, pady=(12, 0))

    def ao_cadastrar(self, callback):
        self.botao_cadastrar.configure(
            command=lambda: callback(self.campo_nome.get(), self.campo_email.get()))

    def ao_fechar(self, callback):
        def fechar():
            callback()
            self.root.destroy()
        self.root.protocol("WM_DELETE_WINDOW", fechar)

    def agendar(self, milissegundos, funcao):
        self.root.after(milissegundos, funcao)

    def executar(self):
        self.root.mainloop()

    def sucesso(self, texto):
        self.rotulo_status.configure(text=texto, foreground="green")

    def erro(self, texto):
        self.rotulo_status.configure(text=texto, foreground="red")

    def cadastro_concluido(self):
        self.campo_nome.configure(state="disabled")
        self.campo_email.configure(state="disabled")
        self.botao_cadastrar.configure(state="disabled")

    def mostrar_token(self, chave, expira_em, novo):
        self.rotulo_token.configure(text=chave)
        situacao = "novo token gerado" if novo else "token mantido"
        self.sucesso(f"Servidor respondeu: {situacao}.")
        self.segundos = expira_em
        if self.contagem_id is not None:
            self.root.after_cancel(self.contagem_id)
        self._contagem()

    def _contagem(self):
        self.rotulo_validade.configure(text=f"Expira em {self.segundos}s")
        if self.segundos > 0:
            self.segundos -= 1
            self.contagem_id = self.root.after(1000, self._contagem)

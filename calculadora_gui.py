import tkinter as tk

from calculadora import somar, subtrair, multiplicar, dividir


class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display_var = tk.StringVar(value="0")
        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = True

        display = tk.Entry(
            master,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            state="readonly",
            readonlybackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        botoes = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for texto, linha, coluna in botoes:
            comando = lambda t=texto: self.ao_clicar(t)
            tk.Button(master, text=texto, font=("Arial", 18), command=comando).grid(
                row=linha, column=coluna, sticky="nsew", padx=2, pady=2
            )

        for i in range(5):
            master.rowconfigure(i, weight=1)
        for i in range(4):
            master.columnconfigure(i, weight=1)

    def ao_clicar(self, texto):
        if texto.isdigit():
            self.digitar_numero(texto)
        elif texto == "C":
            self.limpar()
        elif texto in ("+", "-", "*", "/"):
            self.definir_operacao(texto)
        elif texto == "=":
            self.calcular()

    def digitar_numero(self, digito):
        if self.novo_numero:
            self.display_var.set(digito)
            self.novo_numero = False
        else:
            self.display_var.set(self.display_var.get() + digito)

    def limpar(self):
        self.display_var.set("0")
        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = True

    def definir_operacao(self, operacao):
        self.primeiro_numero = float(self.display_var.get())
        self.operacao = operacao
        self.novo_numero = True

    def calcular(self):
        if self.primeiro_numero is None or self.operacao is None:
            return

        segundo_numero = float(self.display_var.get())
        funcoes = {"+": somar, "-": subtrair, "*": multiplicar, "/": dividir}

        try:
            resultado = funcoes[self.operacao](self.primeiro_numero, segundo_numero)
            self.display_var.set(str(resultado))
        except ValueError:
            self.display_var.set("Erro")

        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = True


if __name__ == "__main__":
    root = tk.Tk()
    CalculadoraApp(root)
    root.mainloop()

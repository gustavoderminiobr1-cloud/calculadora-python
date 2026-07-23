from calculadora import somar, subtrair, multiplicar, dividir


class CalculadoraController:
    def __init__(self, display_var):
        self.display_var = display_var
        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = True

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

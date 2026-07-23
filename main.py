from calculadora import somar, subtrair, multiplicar, dividir


def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.")


def main():
    operacoes = {
        "1": ("Somar", somar),
        "2": ("Subtrair", subtrair),
        "3": ("Multiplicar", multiplicar),
        "4": ("Dividir", dividir),
    }

    print("=== Calculadora ===")
    for chave, (nome, _) in operacoes.items():
        print(f"{chave}. {nome}")

    escolha = input("Escolha uma operação (1-4): ").strip()

    if escolha not in operacoes:
        print("Opção inválida.")
        return

    nome, funcao = operacoes[escolha]
    a = pedir_numero("Digite o primeiro número: ")
    b = pedir_numero("Digite o segundo número: ")

    try:
        resultado = funcao(a, b)
        print(f"Resultado: {resultado}")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()

import os


def proximo_fibonacci(a, b):
    return a + b


def gravar_termo(nome_arquivo, conteudo, modo):
    with open(nome_arquivo, modo, encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


def main():
    caminho = "C:/temp/fibonacci.txt"

    # garante diretório
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    a = 0
    b = 1

    quantidade = 20  # quantidade de termos

    for i in range(quantidade):
        linha = f"{a}\n"
        print(linha, end="")

        # primeiro termo -> sobrescreve
        if i == 0:
            gravar_termo(caminho, linha, "w")
        else:
            gravar_termo(caminho, linha, "a")

        # próximo termo
        b = proximo_fibonacci(a, b)
        a, b = b, a


if __name__ == "__main__":
    main()
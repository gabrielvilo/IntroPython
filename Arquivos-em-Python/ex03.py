import os


def verificar_impar(numero):
    if numero % 2 != 0:
        return numero
    else:
        return -1


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()


def main():
    caminho = "C:/temp/fibonacci.txt"

    # verifica se o arquivo existe
    if not os.path.exists(caminho):
        print("Arquivo não encontrado!")
        return

    linhas = ler_arquivo(caminho)

    for linha in linhas:
        numero = int(linha.strip())
        resultado = verificar_impar(numero)

        if resultado != -1:
            print(resultado)


if __name__ == "__main__":
    main()
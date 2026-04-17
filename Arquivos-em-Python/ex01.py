import os


def calcular_quadrado(numero):
    return numero ** 2


def gravar_arquivo(nome_arquivo, conteudo):
    
    diretorio = os.path.dirname(nome_arquivo)
    os.makedirs(diretorio, exist_ok=True)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


def main():
    resultado = ""

    for i in range(10, 151):
        quadrado = calcular_quadrado(i)
        linha = f"{i} ao quadrado = {quadrado}\n"
        
        print(linha, end="")
        resultado += linha

    caminho = "C:/temp/ex31.txt"
    gravar_arquivo(caminho, resultado)


if __name__ == "__main__":
    main()
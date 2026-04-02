import os

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

def criar_diretorio():
    global dir
    dir = '/tmp/exercicios'

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

def med(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

def escreveArq(caminho, arquivo, linha_arq):
    file = ''
    tipo = ''
    enc = 'utf-8'

    if os.path.exists(caminho) and os.path.isdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)

        if not os.path.exists(caminho_completo):
            tipo = 'w'
        else:
            tipo = 'a'

        file = open(caminho_completo, tipo, encoding=enc)
        file.write(linha_arq)
        file.close()

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    dir = '/tmp/exercicios'
    arq = 'ex21.txt'

    linha = (
        nm + ' : ' +
        str(nt1) + ', ' +
        str(nt2) + ', ' +
        str(nt3) + ', ' +
        str(nt4) + '\n' +
        'média : ' + str(vlr_med) + '\n\n'
    )

    escreveArq(dir, arq, linha)

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input("Digite o nome: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))

    valor_media = med(nota1, nota2, nota3, nota4)

    print(f"Média de {nome}: {valor_media:.2f}")

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    criar_diretorio()

    contador = 0

    caminho = '/tmp/exercicios/ex21.txt'
    if os.path.exists(caminho):
        open(caminho, 'w').close()

    while contador < 5:
        entrada()
        contador += 1

if __name__ == "__main__":
    main()
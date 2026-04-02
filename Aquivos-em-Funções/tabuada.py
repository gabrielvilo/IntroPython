import os

valor = 0
dir = ''
arq = ''

def mult(vlr, tab):
    res = 0
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir, arq

    file = ''
    tipo = ''
    linha = ''

    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):

        caminho = dir + '/' + arq

        if os.path.exists(caminho):
            if c > 0:
                tipo = 'a'
            else:
                tipo = 'w'
        else:
            tipo = 'w'

        file = open(caminho, tipo)
        file.write(linha)
        file.close()

def main():
    global valor, dir, arq

    contador = 0
    result = 0

    dir = '/tmp/exercicios'
    arq = 'ex34.txt'

    valor = int(input("Digite um valor entre 1 e 10: "))

    for contador in range(1, 11):
        result = mult(valor, contador)
        grava(contador, result)

if __name__ == "__main__":

    if not os.path.exists('/tmp/exercicios'):
        os.makedirs('/tmp/exercicios')
        os.chmod('/tmp/exercicios', 0o744)

    main()
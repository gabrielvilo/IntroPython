n1 = 0
n2 = 0

def ler():
    global n1, n2
    n1 = int(input('Insira um número inteiro: '))
    n2 = int(input('Insira um segundo número inteiro: '))

def processar():
    global n1, n2

    if (n1 > n2 and n1 % n2 == 0) or (n2 > n1 and n2 % n1 == 0):
        print('O valor maior é multiplo do menor.')
    else:
        print('O valor maior não é multiplo do menor.')

def main():
    ler()
    processar()

main()
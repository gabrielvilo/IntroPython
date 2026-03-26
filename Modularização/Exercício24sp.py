n1 = 0

def ler():
    global n1
    n1 = int(input('Insira um número inteiro: '))

def processar():
    global n1

    if (n1 % 3 == 0) and (n1 % 2 == 0):
        print('O número é divisível por 2 e 3.')
    elif (n1 % 2 == 0):
        print('O número é divisível por 2.')
    elif (n1 % 3 == 0):
        print('O número é divisível por 3.')
    else:
        print('O número não é divisível nem por 2 nem por 3.')

def main():
    ler()
    processar()

main()
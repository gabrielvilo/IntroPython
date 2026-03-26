num1 : float = 0
num2 : float = 0

def ler():
    global num1, num2
    num1 = float(input('Digite um valor real: '))
    num2 = float(input('Digite um segundo valor real: '))

def processar():
    global num1, num2

    if (num1 > num2):
        print('O maior número é',num1)
    else:
        print('O maior número é',num2)

def main():
    ler()
    processar()

main()
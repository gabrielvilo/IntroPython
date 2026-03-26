num1 : int = 0
num2 : int = 0
dif : int = 0

def ler():
    global num1, num2
    num1 = int(input('Digite um valor inteiro: '))
    num2 = int(input('Digite um segundo valor inteiro: '))

def processar():
    global num1, num2, dif

    if (num1 > num2):
        dif = (num1 - num2)
    else:
        dif = (num2 - num1)

def mostrar():
    global dif
    print('A diferença dos valores é de: ',dif)

def main():
    ler()
    processar()
    mostrar()

main()

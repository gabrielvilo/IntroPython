num1 : int = 0
num2 : int = 0

def ler():
    global num1, num2
    num1 = int(input('Digite um valor inteiro: '))
    num2 = int(input('Digite um segundo valor: '))

def processar():
    global num1, num2

    if (num1 == num2):
        print('Os números possuem o mesmo valor, portanto, não existe uma ordem')

    elif (num1 > num2):
        print('A ordem crescente dos números é: ',num2,',',num1)

    else:
        print('A ordem crescente dos números é: ',num1,',',num2)

def main():
    ler()
    processar()

main()
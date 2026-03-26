valorA = 0
valorB = 0
valorC = 0
valorD = 0

def ler():
    global valorA, valorB, valorC, valorD
    valorA = int(input("Digite o primeiro valor: "))
    valorB = int(input("Digite o segundo valor: "))
    valorC = int(input("Digite o terceiro valor: "))
    valorD = int(input("Digite o quarto valor: "))

def processar():
    global valorA, valorB, valorC, valorD

    if(valorD < valorA):
        print(valorD, ",", valorA, ",", valorB,",", valorC)
    elif(valorD < valorB):
        print(valorA, ",", valorD, ",", valorB,",", valorC)
    elif(valorD < valorC):
        print(valorA, ",", valorB,",",valorD, "," ,valorC)   
    else:
        print(valorA, ",", valorB,",", valorC , ",", valorD)

def main():
    ler()
    processar()

main()
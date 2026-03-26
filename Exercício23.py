valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))
valorC = int(input("Digite o terceiro valor: "))
valorD = int(input("Digite o quarto valor: "))

if(valorD < valorA):
    print(valorD, ",", valorA, ",", valorB,",", valorC)
elif(valorD < valorB):
    print(valorA, ",", valorD, ",", valorB,",", valorC)
elif(valorD < valorC):
    print(valorA, ",", valorB,",",valorD, "," ,valorC)   
else:
    print(valorA, ",", valorB,",", valorC , ",", valorD)
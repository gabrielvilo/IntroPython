média : float
bim1 = float(input(('Qual foi sua nota bimestre 1?: ')))
bim2 = float(input(('Qual foi sua nota bimestre 2?: ')))
bim3 = float(input(('Qual foi sua nota bimestre 3?: ')))
bim4 = float(input(('Qual foi sua nota bimestre 4?: ')))

média = ((bim1+bim2+bim3+bim4) / 4)

if (média >= 6):
    print('Você foi aprovado!')

elif (média >=3 and média <6):
    print ('Você está abaixo da média esperada, será nescessário realizar uma prova para recuperação.')

else:
    print('Infelizmente você foi reprovado.')
n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira um segundo número inteiro: '))

if (n1 > n2 and n1 % n2 == 0) or (n2 > n1 and n2 % n1 == 0):
    print('O valor maior é multiplo do menor.')
else:
    print('O valor maior não é multiplo do menor.')
num1 : int = 0
num2 : int = 0
dif : int

num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite um segundo valor inteiro: '))

if (num1 > num2):
    dif = (num1 - num2)

else:
    dif = (num2 - num1)

print('A diferença dos valores é de: ',dif)
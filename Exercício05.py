import math

a : float = 0; b : float = 0 ; c : float = 0
x1 : float = 0
x2 : float = 0
delta : float = 0

a = float(input('Defina um valor "a" para uma equação do 2° grau: '))
b = float(input('Agora um valor "b": '))
c = float(input('E, por fim, um valor "c": ')) 

delta = ((b*b) - 4 * a * c)

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print('As raízes da equação são, respectivamente : ',x1,'e',x2)




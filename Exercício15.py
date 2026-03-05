import math

cat1 : float = 0
cat2 : float = 0
hip : float = 0

cat1 = float(input('Defina um valor para o cateto 1: '))
cat2 = float(input('Agora para o cateto 2: '))

hip = (cat1**2+cat2**2)
hip = math.sqrt(hip)

print('O valor da hipotenusa é: ',hip)
x : int = 0
y : int = 0
aux : int = 0

x = int (input('Defina um valor para x: '))
y = int (input('Defina um valor para y: '))

aux = x
x = y
y = aux

print('Invertendo os valores de x e y, agora temos, respectivamente:', x,"e", y)
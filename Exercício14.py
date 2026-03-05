ang1 : int = 0
ang2 : int = 0
ang3 : int = 0

ang1 = int(input('Defina um ângulo para um triângulo: '))
ang2 = int(input('Agora defina um segundo ângulo: '))

ang3 = (180-(ang1+ang2))

print('O valor do ângulo 3 será de:' ,ang3)
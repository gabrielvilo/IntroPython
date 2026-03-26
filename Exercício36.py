n = int(input('Digite um número inteiro: '))
calc : float = 1.0
calc_fat : int = 1

for i in range(1,n+1):
    calc_fat *= i
    calc += 1 / calc_fat

print(f'{calc:.2f}')
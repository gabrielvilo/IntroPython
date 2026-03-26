n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um segundo número inteiro: '))
rs : int = 0

if n1 < n2:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2

for i in range(menor, maior+1):
    if i % 2 != 0:
        rs = rs + i

print(f'O resultado da soma dos números ímpares entre {menor} e {maior} será de {rs}')

maior = 0
menor = 0

for i in range(100):
    num = int(input("Digite um número positivo: "))

    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num

print("Maior valor:", maior)
print("Menor valor:", menor)
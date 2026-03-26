n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um segundo número: '))

if n2 < n1:
    menor = n2
    maior = n1
else:
    maior = n2
    menor = n1

print(f"Os números primos entro os inseridos são:", end=' ')
    
for i in range(menor, maior+1):
    if i > 1:
        div = 0
            
        for ac in range(1, i + 1):
            if i % ac == 0:
                div += 1
            
        if div == 2:
            print(i, end=' ')
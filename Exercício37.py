n = int(input('Digite um número: '))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    prox = a + b
    a = b
    b = prox
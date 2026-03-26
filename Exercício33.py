n1 = int(input('Insira um número inteiro:'))
soma : int = 0
i = 1

while i < n1:
    soma = soma + (1 / i)
    i += 1
    print(f"{soma:.2f}")
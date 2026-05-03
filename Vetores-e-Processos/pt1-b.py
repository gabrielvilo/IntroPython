def coletar_valor(tamanho):
    vetor = []
    for i in range(tamanho):
        num = int(input(f'Digite o {i+1}° número: '))
        vetor.append(num)
    return vetor

def maior_menor(vetor):
    maior = vetor[0]
    menor = vetor[0]

    for num in vetor:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    return maior, menor

def media_valores(vetor):
    soma = 0

    for num in vetor:
        soma += num

    media = soma / len(vetor)
    return media

def main():
    vetor = coletar_valor(100)

    maior, menor = maior_menor(vetor)
    media = media_valores(vetor)

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Média dos valores: {media:.2f}")
    
if __name__ == '__main__':
    main()
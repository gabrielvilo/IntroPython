def coletar_valor(tamanho):
    vetor = []
    for i in range(tamanho):
        num = int(input(f'Digite o {i+1}° número: '))
        vetor.append(num)
    return vetor

def media_intervalo(vetor, inicio = 10, fim = 200):
    soma = 0
    contador = 0

    for num in vetor:
        if inicio <= num <= fim:
            soma += num
            contador += 1

    if contador == 0:
        return None
    
    return soma / contador

def soma_impares(vetor):
    soma = 0

    for num in vetor:
        if num % 2 != 0:
            soma += num

    return soma    

def main():
    vetor = coletar_valor(50)

    media = media_intervalo(vetor)
    soma = soma_impares(vetor)

    if media is not None :
        print(f'Média entre 10 e 200: {media:.2f}')
    else:
        print('Nenhum valor entre 10 e 200 foi digitado.')

    print(f'A soma dos números ímpares é: {soma}')

if __name__ == '__main__':
    main()
def coletar_valor(tamanho):
    vetor = []
    for i in range(tamanho):
        num = float(input(f'Digite a {i+1}° nota: '))
        vetor.append(num)
    return vetor


def media_grupo(vetor):
    soma = 0

    for num in vetor:
        soma += num

    return soma / len(vetor)


def analisar_notas(vetor, media):
    acima_media = 0
    posicoes_abaixo = []

    for i, num in enumerate(vetor):
        if num > media:
            acima_media += 1
        elif num < media:
            posicoes_abaixo.append(i)

    return acima_media, posicoes_abaixo


def main():
    vetor = coletar_valor(30)

    media = media_grupo(vetor)
    acima, abaixo = analisar_notas(vetor, media)

    print(f"Média do grupo: {media:.2f}")
    print(f"Quantidade acima da média: {acima}")
    print(f"Posições abaixo da média: {abaixo}")


if __name__ == '__main__':
    main()
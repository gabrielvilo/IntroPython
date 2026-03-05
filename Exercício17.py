tempo : float = 0
velocidade : float = 0
distância : float = 0
litros : float = 0

tempo = float(input('Quanto tempo foi gasto na viagem?: '))
velocidade = float(input('Qual foi a velocidade média?: '))

distância = (tempo * velocidade)
litros = (distância / 12)

print('A quantidade em litros de combustível consumida foi de: ',litros)
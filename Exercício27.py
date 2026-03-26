voltas = int(input('Quantas voltas foram dadas no circuito?: '))
circuito = int(input('Qual o comprimento do circuito em metros?: '))
tempo = int(input('Qual foi a duração em minutos?: '))

distância = voltas * circuito
vm = (distância / 1000) / (tempo / 60)

print('A velocidade média foi de: ',vm,' km/h')

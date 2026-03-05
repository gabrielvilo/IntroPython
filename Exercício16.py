s : float = 0
ht : float = 0
vh : float = 0
pd : float = 0.08
d : float = 0

ht = float(input('Quantas horas foram trabalhadas?: '))
vh = float(input('Qual o valor da hora trabalhada?: '))
d = float (input('Quantos dependentes você possui?: '))

s = (ht*vh)
s = (s-(s*pd))
s = (s + (100*d))

print('O salário a receber com os descontos e acréscimos por dependentes já incluídos é de: ',s)
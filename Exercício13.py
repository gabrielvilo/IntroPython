kg : float = 0
g : float = 0
dias : int = 0

kg = float(input('Quantos kg de alimentos vc precisa?: '))

g = (kg*1000)
dias = (g/50)

print('Serão necessários', dias,'dias para terminar o consumo dos alimentos comendo 50g por dia')
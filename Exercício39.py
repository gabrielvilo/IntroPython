grãos = 1
total = 0

for i in range(1, 65):
    print(f'Casa {i}: {grãos} grãos')
    total += grãos
    grãos *= 2

print(f'O total de grãos no tabuleiro é de: {total}.')
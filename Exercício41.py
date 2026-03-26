print('As combinações possíveis de um dado com resultado 7 são:')

for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        if dado1 + dado2 == 7:
            print(f"{dado1} + {dado2} = 7")
            
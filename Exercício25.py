hr_i = int(input('Insira a hora em que o jogo inciou (HH): '))
min_i = int(input('Insira o minuto em que o jogo começou (MM): '))
hr_f = int(input('Agora a hora final (HH): '))
min_f = int(input('Minuto final (MM): '))

def main(hr_i, min_i, hr_f, min_f):
    duração = (hr_f * 60 + min_f) - (hr_i * 60 + min_i)
    if (duração < 0):
        duração += 24 * 60

    return duração // 60, duração % 60

h, m = main(hr_i, min_i, hr_f, min_f)

print('O jogo teve', h,'horas e', m, 'minutos.')



hr_i = 0
min_i = 0
hr_f = 0
min_f = 0

def ler():
    global hr_i, min_i, hr_f, min_f
    hr_i = int(input('Insira a hora em que o jogo inciou (HH): '))
    min_i = int(input('Insira o minuto em que o jogo começou (MM): '))
    hr_f = int(input('Agora a hora final (HH): '))
    min_f = int(input('Minuto final (MM): '))

def processar():
    global hr_i, min_i, hr_f, min_f

    duração = (hr_f * 60 + min_f) - (hr_i * 60 + min_i)
    if (duração < 0):
        duração += 24 * 60

    h = duração // 60
    m = duração % 60

    print('O jogo teve', h,'horas e', m, 'minutos.')

def main():
    ler()
    processar()

main()
nascimento : int = 0 
ano : int = 0
idade : int = 0
idade_futura : int = 0

nascimento = int(input('Em que ano você nasceu?: '))
ano = int(input('Em que ano estamos?: '))

idade = (ano - nascimento)
idade_futura = (idade + 17)

print('Sua idade atual é de', idade,"e sua idade daqui 17 anos será de", idade_futura)
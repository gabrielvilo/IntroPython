comprimento : int = 0
altura : int = 0
largura : int = 0
volume : int = 0

comprimento = int (input('Defina o comprimento em centímetros de um paralelepípedo: '))
altura = int (input('Agora a altura do mesmo: '))
largura = int (input("Por fim, sua largura: "))

volume = (comprimento * altura * largura)

print('O volume do paralelepípedo é de em cm³ é de: ', volume)

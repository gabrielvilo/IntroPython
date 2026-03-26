def ler():
    investimento = int (input('Escolha o tipo de inventismento. 1 = Poupança. 2 = Renda fixa. '))
    valor = float(input('Qual será o valor depositado?(Insira os centavos). '))
    processar(investimento, valor)

def processar(investimento, valor):

    if (investimento == 1):
        rendimento = valor * 1.03
        print('O valor total após rendimento de 30 dias é de:', rendimento)
    elif (investimento == 2):
        rendimento = valor * 1.05
        print('O valor total após rendimento de 30 dias é de:', rendimento)
    else:
        print("Insira um investimento válido")

def main():
    ler()

main()
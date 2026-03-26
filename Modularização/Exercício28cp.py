def ler():
    preço_atual = float(input('Insira o preço atual de um produto: '))
    venda_mensal = int (input('Insira o valor de vendas mensais desse produto: '))
    processar(preço_atual, venda_mensal)

def processar(preço_atual, venda_mensal):

    if (venda_mensal < 500) and (preço_atual < 30.00):
        preço_novo = preço_atual * 1.10
        print(f'O novo preço do produto será de: {preço_novo: .2f}')
    elif (venda_mensal >= 500 and venda_mensal < 1000) and (preço_atual >= 30.00 and preço_atual < 80.00):
        preço_novo = preço_atual * 1.15
        print(f'O novo preço do produto será de: {preço_novo: .2f}')
    elif (venda_mensal >= 1000) and (preço_atual >= 80.00):
        preço_novo = preço_atual * 0.95
        print(f'O novo preço do produto será de: {preço_novo: .2f}')
    else:
        print('O produto não terá um novo preço por não se adequar aos requisitos de valor e/ou venda mensal.')

def main():
    ler()

main()
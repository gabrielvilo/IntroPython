import math

A : float = 0
B : float = 0
C : float = 0

def ler():
    global A, B, C
    A = float(input("Digite o coeficiente A: "))
    B = float(input("Digite o coeficiente B: "))
    C = float(input("Digite o coeficiente C: "))

def processar():
    global A, B, C

    if A == 0:
        print("O coeficiente A não pode ser zero em uma equação do 2º grau.")
    else:
        delta = B**2 - 4*A*C
        print(f"O valor de delta é: {delta:.2f}")

        if delta > 0:
            x1 = (-B + math.sqrt(delta)) / (2*A)
            x2 = (-B - math.sqrt(delta)) / (2*A)
            print(f"As raízes reais são: x1 = {x1:.2f} e x2 = {x2:.2f}")
        
        elif delta == 0:
            x = -B / (2*A)
            print(f"Só possui uma raíz real: x = {x:.2f}")
        
        else:
            print("Não possui raízes reais.")

def main():
    ler()
    processar()

main()
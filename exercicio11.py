def calcularS(N):
    S = 0
    fatorial = 1
    for i in range(1, N + 1):
        fatorial *= i
        S += 1 / fatorial
    return S

def main():
    N = int(input("Digite um valor inteiro positivo N: "))
    if N > 0:
        resultado = calcularS(N)
        print("O valor de S para N =", N, "é:", resultado)
    else:
        print("Por favor, digite um valor inteiro positivo.")
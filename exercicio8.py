def calcularFatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return  numero * calcularFatorial(numero - 1)
    
    numero = int(input("Digite um número inteiro positivo: "))

    if numero < 0:
        print("Erro: O número deve ser positivo.")
    else:
        fatorial = calcularFatorial(numro)
        print("O fatorial de", numero, "é:", fatorial)
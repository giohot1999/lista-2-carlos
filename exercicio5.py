def isprimo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def filtrarprimos(vetor):
    return [num for num in vetor if isprimo(num)]

def main():
    vetor = [int(input(f"Digite o número {i+1}: ")) for i in range(15)]
    primos = filtrarprimos(vetor)
    print("\nNúmeros primos encontrados:", primos)
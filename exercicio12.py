def ultimoNome(nomeCompleto):
    partesNome = nomeCompleto.split()
    return partesNome[-1]

def main():
    nomeCompleto = input("Digite o nome completo da pessoa: ")
    ultimo = ultimoNome(nomeCompleto)
    print("O último nome é:", ultimo)
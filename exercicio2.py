def encontrarElemento(vetor, elemento):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            posicoes.append(i)
    return posicoes

def verificarElemento30(vetor):
    elementos30 = encontrarElemento(vetor, 30)
    if elementos30:
        print("Elemento 30 encontrado nas posições:", elementos30)
    else:
        print("Nenhum elemento igual a 30 encontrado no vetor.")

def main():
    vetor = [10, 20, 30, 40, 50, 30, 60, 70, 80, 30, 90, 30, 100, 110, 30]
    verificar_elemento_igual_30(vetor)
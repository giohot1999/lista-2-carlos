def calcularQuantidadePrecoInferior(precoProdutos):
    quantidade = 0
    for preco in precoProdutos:
        if preco < 50:
            quantidade += 1
    return quantidade

def encontrarProdutosEntrePrecos(produtos, precoProdutos, precoMin, precoMax):
    produtosEntrePrecos = []
    for i in range(len(produtos)):
        if precoMin <= precoProdutos[i] <= precoMax:
            produtosEntrePrecos.append(produtos[i])
    return produtosEntrePrecos

def calcularMediaPrecoSuperior(precoProdutos):
    produtosPrecoSuperior = [preco for preco in precoProdutos if preco > 100]
    if produtosPrecoSuperior:
        media = sum(produtosPrecoSuperior) / len(produtosPrecoSuperior)
        return media
    else:
        return 0

def main():
    produtos = []
    precoProdutos = []

    for i in range(5):
        produto = input("Digite o nome do produto {}: ".format(i+1))
        preco = float(input("Digite o preço do produto {}: ".format(i+1)))
        produtos.append(produto)
        precoProdutos.append(preco)

    quantidadePrecoInferior50 = calcularQuantidadePrecoInferior(precoProdutos)
    produtosEntre50e100 = encontrarProdutosEntrePrecos(produtos, precoProdutos, 50, 100)
    mediaPrecoSuperior100 = calcularMediaPrecoSuperior(precoProdutos)

    print("\nQuantidade de produtos com preço inferior a R$ 50,00:", quantidadePrecoInferior50)
    print("Produtos com preço entre R$ 50,00 e R$ 100,00:", produtosEntre50e100)
    print("Média dos preços dos produtos com preço superior a R$ 100,00: R$", mediaPrecoSuperior100)
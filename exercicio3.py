def calcularComissao(vendas, comissao):
    comissoes = []
    for i in range(len(vendas)):
        comissoes.append(vendas[i] * comissao[i] / 100)
    return comissoes

def receberDadosVendedores():
    vendas = []
    comissoes = []
    nomes = []
    for i in range(10):
        nome = input("Digite o nome do vendedor {}: ".format(i+1))
        nomes.append(nome)
        venda = float(input("Digite o total de vendas do vendedor {}: ".format(nome)))
        vendas.append(venda)
        comissao = float(input("Digite o percentual de comissão do vendedor {} (%): ".format(nome)))
        comissoes.append(comissao)
    return vendas, comissoes, nomes

def main():
    vendas, comissoes, nomes = receberDadosVendedores()
    comissoesCalculadas = calcularComissao(vendas, comissoes)
    
    print("\nRelatório de Comissões:")
    total_vendas = sum(vendas)
    print("Total de vendas de todos os vendedores: R${}".format(totalVendas))
    
    maiorComissao = max(comissoesCalculadas)
    menorComissao = min(comissoesCalculadas)
    maiorIndex = comissoesCalculadas.index(maiorComissao)
    menorIndex = comissoesCalculadas.index(menorComissao)
    
    print("Maior valor a receber: R${} (Vendedor: {})".format(maiorComissao, nomes[maiorIndex]))
    print("Menor valor a receber: R${} (Vendedor: {})".format(menorComissao, nomes[menorIndex]))
    
    print("\nRelatório de Vendedores e Valores a Receber:")
    for i in range(10):
        print("Vendedor: {}, Valor a Receber: R${}".format(nomes[i], comissoesCalculadas[i]))
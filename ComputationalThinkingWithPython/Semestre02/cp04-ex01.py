estoque = (("TV", (1500.0, 3)),    ("Geladeira", (2000.0, 2)),    ("Microondas", (800.0, 5)))

def consultar_estoque(estoque):
    '''
    Le os valores dentro da variavel, mostrando ao usuario atraves do print uma lista de item, preco, quantidade no estoque e o valor total de cada item e o valor total de todos os itens
    '''
    total = 0
    for itens in estoque:
        nome, valores = itens
        print(f"\n************************\nProduto: {nome}\n - Preço: ${valores[0]}\n - total: {valores[1]}\n ---------\nValor total de {nome}(s) em estoque: ${valores[0]*valores[1]}")
        total += (valores[0]*valores[1])
    
    print(f"\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\nValor total de todos os produtos em estoque: ${total}")



consultar_estoque(estoque)
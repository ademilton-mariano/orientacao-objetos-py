class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado ao pedido.")

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
            
        return total
        

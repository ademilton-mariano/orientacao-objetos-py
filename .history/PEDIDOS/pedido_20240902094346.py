class Pedido:
    
    # Método construtor
    def __init__(self):
        self.produtos = []

    # Método para adicionar um produto ao pedido
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado ao pedido.")

    # Método para calcular o valor total do pedido
    def calcular_total(self):
        
        # Variável para armazenar o valor total do pedido
        total = 0
        
        # Percorre a lista de produtos
        for produto in self.produtos:
            
            # Soma o preço de cada produto ao valor total
            total += produto.preco
        
        # Retorna o valor total do pedido  
        return total
        

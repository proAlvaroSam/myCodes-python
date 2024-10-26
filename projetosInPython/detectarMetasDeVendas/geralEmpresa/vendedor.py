class Vendedor:
    def __init__(self, nome, quantidade_vendas, valor_vendas):
        self.nome = nome.title()
        self.quantidade_vendas = quantidade_vendas
        self.valor_vendas = valor_vendas
    
    def atingiu_meta(self, meta_vendas):
        return self.valor_vendas >= meta_vendas
    
    def __str__(self):
        return f"{self.nome} - {self.quantidade_vendas} vendas - R${self.valor_vendas}"

from geralEmpresa.vendedor import Vendedor
from tabulate import tabulate

class Empresa:
    def __init__(self, meta_vendas):
        self.meta_vendas = meta_vendas
        self.vendedores = []
    
    def adicionar_vendedor(self, vendedor):
        self.vendedores.append(vendedor)
    
    def listar_vendedores(self):
        headers = ["Nome do vendedor", "Quantidade de Vendas", "Valor das Vendas"]
        table = [[vendedor.nome, vendedor.quantidade_vendas, vendedor.valor_vendas] for vendedor in self.vendedores]
        print(tabulate(table, headers, tablefmt="grid"))
    
    def listar_vendedores_que_atingiram_meta(self):
        headers = ["Nome do vendedor", "Quantidade de Vendas", "Valor das Vendas"]
        table = [[vendedor.nome, vendedor.quantidade_vendas, vendedor.valor_vendas] for vendedor in self.vendedores if vendedor.atingiu_meta(self.meta_vendas)]
        print("Vendedores que atingiram a meta:")
        print(tabulate(table, headers, tablefmt="grid"))

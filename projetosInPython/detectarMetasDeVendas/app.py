from geralEmpresa.empresa import Empresa
from geralEmpresa.vendedor import Vendedor

def main():
    meta_vendas = 10000
    empresa = Empresa(meta_vendas)
    
    vendedor1 = Vendedor('Alice', 150, 12000)
    vendedor2 = Vendedor('Bob', 80, 5000)
    vendedor3 = Vendedor('Carlos', 100, 9500)
    
    empresa.adicionar_vendedor(vendedor1)
    empresa.adicionar_vendedor(vendedor2)
    empresa.adicionar_vendedor(vendedor3)
    
    print("Todos os vendedores:")
    empresa.listar_vendedores()
    print()  # Linha em branco para separar as listas
    empresa.listar_vendedores_que_atingiram_meta()

if __name__ == '__main__':
    main()
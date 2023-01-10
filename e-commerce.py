from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('------------------------------------------')
    print('----------  BEM VINDO(A) -----------------')
    print('-------------  Z-TECH  ------------------')
    print('------------------------------------------')
    print('------------------------------------------')
   
    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_Carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print(" Obrigado pela preferência. Volte sempre! ")
        sleep(2)
        exit(0)
    else:
        print('Opção inválida ')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print(' Cadastramento de Produto')
    print('-------------------------')

    nome: str = input('Nome do produto: ')
    preco: float = float(input('Preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)
    
    print(f'O produto {produto.nome} foi cadastrado com sucesso! ')
    sleep(1)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0: 
        print(' Informe o código do produto que deseja adicionar ao carrinho; ')
        print('---------------------------------------------------------------')
        print('---------------------Produtos Disponiveis----------------------')
        for produto in produtos:
            print(produto)
            print('-----------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())
        produto: produto = produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f' o produto {produto.nome} agora possui {quant+1} unidades no carrinho. ')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho. ')
                    sleep(2)
                    menu()
                        
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho. ')
                sleep(2)
                menu()
        else:
            print(' O produto com o codigo {codigo} não foi encontrado. ')
            sleep(2)
            menu()
    else:
        print('Não existem produtos para a venda. ')
        sleep(2)
        menu()

def visualizar_Carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('------------------------')
                sleep(2)
                menu()
                
    else:
        print('Não existem produtos no carrinho. ')
        sleep(2)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total +=dados[0].preco * dados[1]
                print('-------------------------------------')
                sleep(2)
        print(f'sua fatura é {formata_float_str_moeda(valor_total)}')
        carrinho.clear()
        sleep(5)
        menu()
    else:
        print('Não existem produtos no carrinho. ')
        sleep(2)
        menu()

def produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    
    for produto in produtos: 
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main() 
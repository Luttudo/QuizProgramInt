import json

# Lista de produtos (simulando o banco de dados)
produtos = []

def adicionar_produto(nome, descricao, preco, estoque):
    produto = {
        'nome': nome,
        'descricao': descricao,
        'preco': preco,
        'estoque': estoque
    }
    produtos.append(produto)

def listar_produtos():
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Estoque: {produto['estoque']}")

def main():
    while True:
        print("\n1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            adicionar_produto(nome, descricao, preco, estoque)
            print("Produto adicionado com sucesso!")
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

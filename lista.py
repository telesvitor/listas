produtos = [
    [1, "Notebook", 3500.00],
    [2, "Smartphone", 1500.00],
    [3, "Mouse Gamer", 150.00],
    [4, "Teclado Mecânico", 350.00]
]

def exibir_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f}")
    print("-" * 25)

while True:
    print("\n====== MENU ======")
    print("1. Imprimir produtos")
    print("2. Localizar produto por ID")
    print("3. Remover produto por ID")
    print("4. [Desafio] Cadastrar novo produto")
    print("5. [Desafio] Alterar preço de um produto")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_produtos()

    elif opcao == "2":
        id_busca = int(input("Digite o ID do produto que deseja buscar: "))
        encontrado = False
        
        for p in produtos:
            if p[0] == id_busca:
                print(f"\nProduto Encontrado -> ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f}")
                encontrado = True
                break
        
        if not encontrado:
            print(f"\nProduto com ID {id_busca} não foi encontrado.")

    elif opcao == "3":
        id_remover = int(input("Digite o ID do produto que deseja remover: "))
        encontrado = False
        
        for p in produtos:
            if p[0] == id_remover:
                produtos.remove(p)
                print(f"\nProduto '{p[1]}' removido com sucesso!")
                encontrado = True
                break
                
        if not encontrado:
            print(f"\nProduto com ID {id_remover} não existe.")
        else:
            exibir_produtos()

    elif opcao == "4":
        print("\n--- CADASTRAR NOVO PRODUTO ---")
        novo_id = int(input("Digite o ID do novo produto: "))
        
        id_existe = any(p[0] == novo_id for p in produtos)
        
        if id_existe:
            print("Erro: Já existe um produto com este ID.")
        else:
            novo_nome = input("Digite o nome do produto: ")
            novo_preco = float(input("Digite o preço do produto: "))
            
            produtos.append([novo_id, novo_nome, novo_preco])
            print(f"\nProduto '{novo_nome}' cadastrado com sucesso!")

    elif opcao == "5":
        print("\n--- ALTERAR PREÇO ---")
        id_alterar = int(input("Digite o ID do produto: "))
        encontrado = False
        
        for p in produtos:
            if p[0] == id_alterar:
                novo_preco = float(input(f"Digite o novo preço para '{p[1]}' (Preço atual: R$ {p[2]:.2f}): "))
                p[2] = novo_preco
                print(f"\nPreço do produto '{p[1]}' atualizado para R$ {novo_preco:.2f}!")
                encontrado = True
                break
                
        if not encontrado:
            print(f"\nProduto com ID {id_alterar} não encontrado.")

    elif opcao == "6":
        print("\nPrograma encerrado. Até mais!")
        break
        
    else:
        print("\nOpção inválida! Tente novamente.")

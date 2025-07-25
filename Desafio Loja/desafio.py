jogos_disponiveis = ["Super Mario Bros", "Zelda", "Minecraft", "King of Fighters"]
preco_produtos = [30.00, 15.00, 23.00, 25.00]
quantidade_produtos = [40, 60, 25, 30]
preco_fabrica = [25.00, 30.00, 50.00, 70.00]
vendas = [0, 0, 0, 0]
compra_estoque = [0, 0, 0, 0]

while True:
    print("\n" + "=" * 40)
    print("✨  Akira's Store  ✨")
    print("=" * 40)
    print(" Seja Bem vindo! Selecione uma das opções abaixo: ")
    print("1 - Registrar Venda")
    print("2 - Compra de estoque")
    print("3 - Resumo da loja")
    print("4 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 1:
        print("\n--- Registrar Venda ---")
        for i, jogo in enumerate(jogos_disponiveis):
            print(f"{i+1} - {jogo} (R${preco_produtos[i]} | Estoque: {quantidade_produtos[i]})")
        try:
            escolha = int(input("Escolha o número do jogo vendido: ")) - 1
            quantidade = int(input("Quantidade vendida: "))
            if 0 <= escolha < len(jogos_disponiveis) and quantidade <= quantidade_produtos[escolha]:
                quantidade_produtos[escolha] -= quantidade
                vendas[escolha] += quantidade
                print("Venda registrada com sucesso!")
            else:
                print("Opção inválida ou estoque insuficiente.")
        except ValueError:
            print("Erro de entrada. Digite números válidos.")

    elif opcao == 2:
        print("\n--- Compra de Estoque ---")
        for i, jogo in enumerate(jogos_disponiveis):
            print(f"{i+1} - {jogo} (Estoque atual: {quantidade_produtos[i]})")
        try:
            escolha = int(input("Escolha o número do jogo para repor estoque: ")) - 1
            quantidade = int(input("Quantidade comprada: "))
            if 0 <= escolha < len(jogos_disponiveis):
                quantidade_produtos[escolha] += quantidade
                compra_estoque[escolha] += quantidade
                print("Estoque atualizado com sucesso!")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro de entrada. Digite números válidos.")

    elif opcao == 3:
        print("\n--- Resumo da Loja ---")
        for i in range(len(jogos_disponiveis)):
            print(f"{jogos_disponiveis[i]} | Preço: R${preco_produtos[i]} | Estoque: {quantidade_produtos[i]} | Vendidos: {vendas[i]} | Comprados: {compra_estoque[i]}")
    elif opcao == 4:
        print("Caixa fechado. Loja encerrada.")
        break
    else:
        print("Opção inválida! Tente novamente.")

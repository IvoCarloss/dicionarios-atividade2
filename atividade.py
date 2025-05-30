estoque = {}

qtnd_de_prod = int(input("Informe a quantidade de produtos que deseja cadastrar: "))
for i in range(qtnd_de_prod):
    nome_prod = input("Informe o nome do produto: ")
    qtd_prod = int(input(f"Informe a quantidade do produto: {nome_prod} "))
    estoque[nome_prod] = qtd_prod

for produto, quantidade in estoque.items():
    print("Produto:", produto, "Quantidade:", quantidade)

busca = input("Informe o nome do produto que deseja pesquisar: ")

if busca in estoque:
    print(f"A quantidade do produto {busca} é {estoque[busca]} ")

    po = int(input("Você quer atualizar seu pedido? 1  adição 2 remoção: "))

    if po == 1:
        c = int(input(f"Quanto você quer adicionar no seu pedido de {busca}? "))
        estoque[busca] += c
        print(f"Resultado da adição agora temos {estoque[busca]} unidades de {busca}")

    elif po == 2:
        c1 = int(input(f"Quanto você quer remover do seu pedido de {busca}? "))
        if c1 <= estoque[busca]:
            estoque[busca] -= c1
            print(f"Resultado da remoção: agora temos {estoque[busca]} unidades de {busca}")
        else:
            print("Erro você tentou remover mais do que tem no estoque")

    else:
        print("Opção inválida")

else:
    print("O produto não está no estoque")

# Dicionário para guardar os filmes
catalogo = {}

# 1. Cadastro de filmes
qtd = int(input("Quantos filmes deseja adicionar ao catálogo? "))

for i in range(qtd):
    titulo = input(f"Digite o título do {i+1}º filme: ")
    ano = int(input(f"Digite o ano de lançamento de '{titulo}': "))
    catalogo[titulo] = ano  # 3. Guardando no dicionário

# 4. Mostrar todos os filmes
print("\n--- Catálogo de Filmes ---")
for titulo, ano in catalogo.items():
    print(f"{titulo} - Lançado em {ano}")

# 5. Buscar um filme pelo título
busca = input("\nDigite o título de um filme para buscar: ")

if busca in catalogo:
    print(f"O filme '{busca}' foi lançado em {catalogo[busca]}.")
else:
    print("Filme não encontrado no catálogo.")

# Desafio Extra: Filtrar filmes por ano
filtro_ano = int(input("\nDeseja ver filmes lançados a partir de qual ano? "))
print(f"\nFilmes lançados a partir de {filtro_ano}:")
encontrados = False

for titulo, ano in catalogo.items():
    if ano >= filtro_ano:
        print(f"{titulo} - {ano}")
        encontrados = True

if not encontrados:
    print("Nenhum filme encontrado nesse período.")

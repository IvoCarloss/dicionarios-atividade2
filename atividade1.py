boletim = {}


qtd = int(input("Quantos alunos deseja cadastrar? "))
for _ in range(qtd):
    nome = input("Nome do aluno: ")
    nota = float(input(f"Nota final de {nome} 0 a 10: "))
    boletim[nome] = nota


print("Boletim:")
for nome, nota in boletim.items():
    print(f"{nome}: {nota}")

while True:
    busca = input("Consultar nota de qual aluno? ou 'sair': ")
    if busca.lower() == 'sair':
        break
    elif busca in boletim:
        print(f"Nota de {busca}: {boletim[busca]}")
    else:
        print("Aluno não encontrado")

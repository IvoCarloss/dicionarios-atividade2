
projetos = []

def cadastrar_projeto():
    nome = input("Nome do projeto: ")
    responsavel = input("Nome do responsavel: ")
    horas = int(input("Horas estimadas: "))
    status = input("Status ativo/finalizado: ").lower()

    projeto = {
        "nome": nome,
        "responsavel": responsavel,
        "horas": horas,
        "status": status
    }

    projetos.append(projeto)
    print("Projeto cadastrado com sucesso")

def listar_projetos():
    if not projetos:
        print("Nenhum projeto cadastrado")
        return
    for i, p in enumerate(projetos, 1):
        print(f"{i}. {p['nome']} | Responsável: {p['responsavel']} | Horas: {p['horas']} | Status: {p['status']}")
    print()

def buscar_por_responsavel():
    nome = input("Digite o nome do responsavel: ")
    encontrados = [p for p in projetos if p["responsavel"].lower() == nome.lower()]
    
    if encontrados:
        for p in encontrados:
            print(f"{p['nome']} | Horas: {p['horas']} | Status: {p['status']}")
    else:
        print("Nenhum projeto encontrado para esse responsavel")
    print()

def mostrar_por_status(status_desejado):
    encontrados = [p for p in projetos if p["status"] == status_desejado]
    
    if encontrados:
        for p in encontrados:
            print(f"{p['nome']} | Responsável: {p['responsavel']} | Horas: {p['horas']}")
    else:
        print(f"Nenhum projeto com status '{status_desejado}'.")
    print()


while True:
    print("MENU")
    print("1 - Cadastrar novo projeto")
    print("2 - Listar todos os projetos")
    print("3 - Buscar por responsável")
    print("4 - Mostrar projetos ATIVOS")
    print("5 - Mostrar projetos FINALIZADOS")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_projeto()
    elif opcao == "2":
        listar_projetos()
    elif opcao == "3":
        buscar_por_responsavel()
    elif opcao == "4":
        mostrar_por_status("ativo")
    elif opcao == "5":
        mostrar_por_status("finalizado")
    elif opcao == "6":
        print("Encerrando o sistema")
        break
    else:
        print("Opção inválida")


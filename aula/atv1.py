print("Menu de opções")
print("1. Adicionar novo cliente.")
print("2. Exibir todos os clientes.")
print("3. Buscar cliente.")
print("4. Atualizar informações.")
print("5. Excluir cliente do sistema.")
opc = int(input("Escreva a opcao: "))

match(opc):
    case 1:
        print("Adicionando items")
    case 2:
        print("Exibindo clientes")
    case 3:
        print("Buscando clientes")
    case 4:
        print("Atualizando clientes")
    case 5:
        print("Excluindo cliente do sistema")
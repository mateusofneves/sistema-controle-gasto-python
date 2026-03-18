#SISTEMA LISTA DE CONTATOS

def limpar_matriz(mm):
    for l in range(10):
        for c in range(3):
            mm[l][c] = ""


#funcao adicionar contato na agenda
def novo(mm, l):
    print("\n-------------------PREENCHA O NOVO CONTATO: ")

    mm[l][0] = input("Nome.........: ")
    mm[l][1] = input("Telefone.....: ")
    mm[l][2] = input("Email........: ")

    print("Contato salvo com sucesso!")


#funcao editar contato ja existente
def editar_contato(mm, l):
    print("\n-------------------EDITE O CONTATO: ")

    mm[l][0] = input("Nome........: ").strip()
    mm[l][1] = input("Telefone....: ").strip()
    mm[l][2] = input("Email.......: ").strip()


#funcao proximo contato se encontrado
def linha_proximo_contato(mm):
    for l in range(10):
        if mm[l][0] == "":
            return l

    return -1


#funcao exibir contato
def exibir_contato(mm, l):
    print(f"Nome:.......... {mm[l][0]}")
    print(f"Telefone....... {mm[l][1]}")
    print(f"Email.......... {mm[l][2]}")


#funcao listar todos os contatos da agenda
def listar_agenda(mm):
    print("\n--------------------------------CONTATOS DA AGENDA: ")

    for l in range(10):
        if mm[l][0] != "":
            exibir_contato(mm, l)
            print("---------------------------------")

    print("\n----------------------FIM DA AGENDA")


#funcao pesquisar contato
def pesquisar_contato(mm, n):
    for l in range(10):
        if mm[l][0].lower().strip() == n.lower().strip():
            return l

    return -1


#funcao excluir linha
def excluir_linhas(mm, l):
    mm[l][0] = ""
    mm[l][1] = ""
    mm[l][2] = ""
    print("Contato Excluído")


#funcao apagar contato
def apagar_contato(mm, n):
    linha = pesquisar_contato(mm, n)

    if linha != -1:
        exibir_contato(mm, linha)
        opcao = input("Confirmar a exclusão do contato?\n [S]im ou [N]ão? ")

        if opcao == "s" or opcao == "S":
            excluir_linhas(mm, linha)
        else:
            print("Exclusão cancelada.")
    else:
        print("Contato não encontrado.")


#esse procedimento lista as opcoes do menu
def exibir_menu():
    print("\n------------ M E N U ------------ ")
    print("[1] - Novo Contato")
    print("[2] - Editar Contato")
    print("[3] - Pesquisar Contato")
    print("[4] - Lista de Contatos")
    print("[5] - Apagar Contato")
    print("[6] - Sair")


#################### PROGRAMA PRINCIPAL ###################
agenda = [["" for _ in range(3)] for _ in range(10)]

opcao = 0

while opcao != 6:
    exibir_menu()
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        posicao = linha_proximo_contato(agenda)
        novo(agenda, posicao)

    if opcao == 2:
        nome = input("Digite o nome para editar: ")
        posicao = pesquisar_contato(agenda, nome)
        if posicao != -1:
            exibir_contato(agenda, posicao)
            editar_contato(agenda, posicao)
        else:
            print("Contato não encontrado.")

    if opcao == 3:
        nome = input("Digite o nome do contato para pesquisar. ")
        posicao = pesquisar_contato(agenda, nome)
        if posicao != -1:
            exibir_contato(agenda, posicao)
        else:
            print("Contato não cadastrado.")

    if opcao == 4:
        listar_agenda(agenda)

    if opcao == 5:
        nome = input("Digite o nome do contato para excluir. ")
        apagar_contato(agenda, nome)

    if opcao == 6:
        print("Programa finalizado com sucesso!")
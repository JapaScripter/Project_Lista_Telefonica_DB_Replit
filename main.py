import contatos
from os import system

main_message = """Lista de Telefone
----------------------------------
Escolha:
1 - para adicionar novo contato
2 - para pesquisar contato
3 - para atualizar contato
4 - para deletar contato
----------------------------------
"""
nome = str()
telefone = int()

def prompt_add_contato():
    nome = str(input("Coloque o nome completo: "))
    telefone = int(input("Coloque o número de telefone: ".strip()))
    print(f"O nome: {nome} com o telefone: {telefone} foi adicionado com sucesso!")
    contatos.add_contato(nome, telefone)

def prompt_get_contato():
    nome = input("Coloque o nome que deseja pesquisar: ")
    telefone = contatos.get_contato(nome)
    if telefone:
        print(f"O telefone de {nome} é {telefone}")
    else:
        matches = contatos.pesquisar_contatos(nome)
        if matches:
            for k in matches:
                print(f"O telefone de {k} é {matches[k]}")
        else:
            print(f"Esse nome: {nome} não está cadastrado!")

def prompt_atualizar_contato():
    velho_nome = input("Coloque o nome que deseja pesquisar: ")
    velho_telefone = contatos.get_contato(velho_nome)
    if velho_telefone:
        novo_nome = input(f"Para qual nome você deseja mudar o {velho_nome} (deixe em branco se nãp quiser mudar): ").strip()
        novo_telefone = input(f"Para qual telefone você deseja mudar o {velho_telefone} (deixe em branco se nãp quiser mudar): ").strip()

        if not novo_telefone:
            novo_telefone = velho_telefone

        if not novo_nome:
            contatos.atualizar_telefone(velho_nome, novo_telefone)
        else:
            contatos.atualizar_contato(velho_nome, novo_nome, novo_telefone)
    else:
        print(f"Esse nome: {velho_nome} não está cadastrado!")
			
def prompt_delete_contato():
    nome = input("Coloque o nome que deseja deletar: ")
    contato = contatos.get_contato(nome)
    if contato:
        print(f"Deleting {nome}")
        contatos.delete_contato(nome)
    else:
        print(f"Esse nome: {nome} não está cadastrado!")

def main():
    print(main_message)
    choice = input("Escolha uma das opções: ").strip()
    if choice == "1":
        prompt_add_contato()
    elif choice == "2":
        prompt_get_contato()
    elif choice == "3":
        prompt_atualizar_contato()
    elif choice == "4":
        prompt_delete_contato()
    else:
        print("Valor inválido. Por favor tente de novo.")

while True:
    system('clear')
    main()
    input("Aperte enter para continuar: ")
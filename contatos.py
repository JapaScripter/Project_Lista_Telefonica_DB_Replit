from replit import db 

def add_contato(nome, numero_telefone):
    if nome in db:
        print("Nome já existe!")
    else:
        db[nome] = limit_phone_number(numero_telefone)

def limit_phone_number(phone_number):
    return phone_number[:10]

def get_contato(nome):
    telefone = db.get(nome)
    return telefone

def pesquisar_contatos(pesquisar):
    matches = {}
    for key in db.keys():
        if key.lower().startswith(pesquisar.lower()):
            matches[key] = db[key]
    return matches

def atualizar_telefone(velho_nome, novo_telefone):
    db[velho_nome] = novo_telefone

def atualizar_contato(velho_nome, novo_nome, novo_telefone):
    db[novo_nome] = novo_telefone
    del db[velho_nome]

def delete_contato(nome):
    del db[nome]

def delete_all_contatos():
    for key in db.keys():
        del db[key]
from replit import db 

def add_contato(nome, numero_telefone):
    if nome in db:
        print("Nome já existe!")
    else:
        db[nome] = numero_telefone

def get_contato(nome):
    telefone = db.get(nome)
    return telefone

def pesquisar_contatos(pesquisar):
    match_keys = db.prefix(pesquisar)
    return {k: db[k] for k in match_keys}

def atualizar_telefone(velho_nome, novo_telefone):
    db[velho_nome] = novo_telefone

def atualizar_contato(velho_nome, novo_nome, novo_telefone):
    db[novo_nome] = novo_telefone
    del db[velho_nome]

def delete_contato(nome):
    del db[nome]
import re 

def lexer(src):
    lista_tokens = []
    doc =  open(src, "r")
    txt = doc.read()
    lista_str = re.split(r'\s+', txt)
    for i in lista_str:
        lista_tokens[i] = id(i)

    return lista_tokens

def id(termino):
    if checkDef(termino):
        tipo = "DEF"
        return tipo
    else:
        return False


lexer("maquina-virtual.txt")


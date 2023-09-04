import re 

O = ["north", "south", "west", "east"]

def lexer(src):
    lista_tokens = []
    doc =  open(src, "r")
    txt = doc.read()
    lista_str = re.split(r'\s+', txt)
    for i in lista_str:
        lista_tokens[i] = id(i)

    return lista_tokens

def id(termino):
    if checkDefVar(termino):
        tipo = "DEFV"
    elif checkDefProc(termino):
        tipo = "DEFP"
    elif checkOpenBr(termino):
        tipo = "{"
    elif checkCloseBr(termino):
        tipo = "}"
    elif checkSep(termino):
        tipo = ";"
    elif checkEquals(termino):
        tipo = "EQ"
    elif checkO(termino):
        tipo = "O"
    else:
        tipo = False
    return tipo

def checkDefVar(termino):
    return termino.lower() == "defvar"

def checkDefProc(termino):
    return termino.lower() == "defproc"

def checkOpenBr(termino):
    return termino.lower() == "{"

def checkCloseBr(termino):
    return termino.lower() == "}"

def checkSep(termino):
    return termino.lower() == ";"

def checkEquals(termino):
    return termino.lower() == "="

def checkO(termino):
    return termino.lower() in O


lexer("maquina-virtual.txt")


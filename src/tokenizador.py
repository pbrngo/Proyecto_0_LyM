import re 

O = ["north", "south", "west", "east"]
S = ["left", "right"]
TURN = ["around"]
ADV = ["front", "back"]
def lexer(src):
    lista_tokens = []
    doc =  open(src, "r")
    txt = doc.read()
    lista_str = re.split(r'\s+', txt)
    for i in lista_str:
        lista_tokens.append(id(i))

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
    elif checkS(termino):
        tipo = "S"
    elif checkV(termino):
        tipo = "V"
    elif checkTurn(termino):
        tipo = "TURN"
    elif checkAdv(termino):
        tipo = "ADV"
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

def checkS(termino):
    return termino.lower() in S

def checkV(termino):
    return termino.isdigit()

def checkTurn(termino):
    return termino.lower() in TURN

def checkAdv(termino):
    return termino.lower() in ADV


print(lexer("maquina-virtual.txt"))


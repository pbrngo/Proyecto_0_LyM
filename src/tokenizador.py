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
    elif checkIf(termino):
        tipo = "IF"
    elif checkElse(termino):
        tipo = "ELS"
    elif checkWhile(termino):
        tipo = "WHL"
    elif checkRepeat(termino):
        tipo = "RPT"
    elif checkIf(termino):
        tipo = "TMS"
    elif checkParametro(termino):
        lista_parametros_token = []
        termino = termino[1:-1]
        lista_parametros = termino.split(",")
        for i in lista_parametros:
            lista_parametros_token.append(id(i))
        tipo = lista_parametros_token[0:-1]
    elif checkParentesis(termino):
        lista_parentesis_token = []
        lista_parentesis = re.split(r'[()]', termino)
        for i in lista_parentesis:
            lista_parentesis_token.append(id(i))
        tipo = lista_parentesis_token[0:-1]
    else:
        tipo = termino
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

def checkIf(termino):
    return termino.lower() == "if"

def checkElse(termino):
    return termino.lower() == "else"

def checkWhile(termino):
    return termino.lower() == "while"

def checkRepeat(termino):
    return termino.lower() == "repeat"

def checkTimes(termino):
    return termino.lower() == "times"

def checkParametro(termino):
    return re.match(r'^\(.+\)$', termino)

def checkParentesis(termino):
    return "(" in termino



print(lexer("maquina-virtual.txt"))


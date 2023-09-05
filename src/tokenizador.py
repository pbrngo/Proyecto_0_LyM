import re 

O = ["north", "south", "west", "east"]
S = ["left", "right"]
TURN = ["around"]
ADV = ["front", "back"]
NT = ["north", "south", "west", "east", "left", "right", "around", "front", "back",
    "DEFV", "DEFP", "{", "}", ";", "EQ", "O", "S", "V", "TURN", "ADV", "IF", "ELS",
    "WHL", "RPT", "TMS", "JMP", "WLK", "LP", "TRN", "DRP", "GET", "GRB", "LETGO", 
    "NOP", "TRNTO", "FCN", "CAN", "NOT"]

def lexer(src):
    lista_tokens = []
    lista_tokens_aplanada = []
    doc =  open(src, "r")
    txt = doc.read()
    lista_str = re.split(r'\s+', txt)
    for i in lista_str:
        lista_tokens.append(id(i))
    for e in lista_tokens:
        if type(e) == list:
            for a in e:
                lista_tokens_aplanada.append(a)
        else:
            lista_tokens_aplanada.append(e)
    return lista_tokens_aplanada

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
    elif checkJump(termino):
        tipo = "JMP"
    elif checkWalk(termino):
        tipo = "WLK"
    elif checkLeap(termino):
        tipo = "LP"
    elif checkTurn(termino):
        tipo = "TRN"
    elif checkDrop(termino):
        tipo = "DRP"
    elif checkGet(termino):
        tipo = "GET"
    elif checkGrab(termino):
        tipo = "GRB"
    elif checkLetGo(termino):
        tipo = "LETGO"
    elif checkNop(termino):
        tipo = "NOP"
    elif checkTurnTo(termino):
        tipo = "TRNTO"
    elif checkFacing(termino):
        tipo = "FCN"
    elif checkCan(termino):
        tipo = "CAN"
    elif checkNot(termino):
        tipo = "NOT"
    elif checkParentesisA(termino):
        tipo = "("
    elif checkParentesisC(termino):
        tipo = ")"
    elif checkComa(termino):
        tipo = ","
    elif checkParentesis(termino):
        lista_parentesis_token = []
        lista_parentesis = re.findall(r'[(),]|[^(),]+', termino)
        for i in lista_parentesis:
            param = id(i)
            lista_parentesis_token.append(param)
        tipo = lista_parentesis_token
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

def checkJump(termino):
    return termino.lower() == "jump"

def checkWalk(termino):
    return termino.lower() == "walk"

def checkLeap(termino):
    return termino.lower() == "leap"

def checkTurn(termino):
    return termino.lower() == "turn"

def checkDrop(termino):
    return termino.lower() == "drop"

def checkDrop(termino):
    return termino.lower() == "drop"

def checkGet(termino):
    return termino.lower() == "get"

def checkGrab(termino):
    return termino.lower() == "grab"

def checkLetGo(termino):
    return termino.lower() == "letgo"

def checkNop(termino):
    return termino.lower() == "nop"

def checkTurnTo(termino):
    return termino.lower() == "turnto"

def checkFacing(termino):
    return termino.lower() == "facing"

def checkCan(termino):
    return termino.lower() == "can"

def checkNot(termino):
    return termino.lower() == "not:"

def checkParentesisA(termino):
    return termino.lower() == "("

def checkParentesisC(termino):
    return termino.lower() == ")"

def checkComa(termino):
    return termino.lower() == ","

def checkParentesis(termino):
    return "(" in termino and ")" in termino



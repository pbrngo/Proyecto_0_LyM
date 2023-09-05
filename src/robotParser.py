import re
import tokenizador as tok

nt = ["north", "south", "west", "east", "left", "right", "around", "front", "back",
    "DEFV", "DEFP", "{", "}", ";", "EQ", "O", "S", "V", "TURN", "ADV", "IF", "ELS",
    "WHL", "RPT", "TMS", "JMP", "WLK", "LP", "TRN", "DRP", "GET", "GRB", "LETGO", 
    "NOP", "TRNTO", "FCN", "CAN", "NOT", "parametro"]

var = []

proc = []

def parse(lista_tokens):
#Tres caracteres terminales: Tdefvar, Tdefproc, Tcommand
    lista_tokens = defVar(lista_tokens)
    print(var)
    return lista_tokens



def defVar(lista_tokens):
    i = 0
    while i <= len(lista_tokens) - 2:
        if (lista_tokens[i] == "DEFV" and (lista_tokens[i + 1] not in nt) and lista_tokens[i + 2] == "V"):
            var.append(lista_tokens[i + 1])
            lista_tokens[i:i+3] = ["Tdefvar"]
        i+=1
    return lista_tokens

def defProc(lista_tokens):
    i = 0
    while i <= len(lista_tokens) - 3:
        if (lista_tokens[i] == "DEFP" and (lista_tokens[i + 1] not in nt) and lista_tokens[i + 2] == "parametro" and lista_tokens[i + 3] == "Tcommand"):
            proc.append(lista_tokens[i + 1])
            lista_tokens[i:i+3] = ["Tdefproc"]
        i+=1
    return lista_tokens

def command(lista_tokens):
    i = 0
    while i <= len(lista_tokens) - 1:
        if lista_tokens[i] == "{":
            
def IF(lista_tokens):
    return lista_tokens

def WHL(lista_tokens):
    return lista_tokens

def condition(lista_tokens):
    return lista_tokens

def RPT(lista_tokens):
    return lista_tokens

def TMS(lista_tokens):
    return lista_tokens

def JMP(lista_tokens):
    return lista_tokens

def WLK(lista_tokens):
    return lista_tokens

def LP(lista_tokens):
    return lista_tokens

def TRN(lista_tokens):
    return lista_tokens

def DRP(lista_tokens):
    return lista_tokens

def GET(lista_tokens):
    return lista_tokens

def GRB(lista_tokens):
    return lista_tokens

def LETGO(lista_tokens):
    return lista_tokens

def NOP(lista_tokens):
    return lista_tokens

def TRNTO(lista_tokens):
    return lista_tokens

def FCN(lista_tokens):
    return lista_tokens

def CAN(lista_tokens):
    return lista_tokens

def NOT(lista_tokens):
    return lista_tokens

def parametro(lista_tokens):
    i = 0
    isValid = True
    while i <= len(lista_tokens):
        if (lista_tokens[i] == "("):
            e = i+1
            while lista_tokens[e] != ")" or isValid:
                
                e += 1
            lista_tokens[i:i+3] = ["Tdefproc"]
        i+=1
    return lista_tokens
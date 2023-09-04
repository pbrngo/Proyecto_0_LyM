import re
import tokenizador as tok

nt = ["north", "south", "west", "east", "left", "right", "around", "front", "back",
    "DEFV", "DEFP", "{", "}", ";", "EQ", "O", "S", "V", "TURN", "ADV", "IF", "ELS",
    "WHL", "RPT", "TMS", "JMP", "WLK", "LP", "TRN", "DRP", "GET", "GRB", "LETGO", 
    "NOP", "TRNTO", "FCN", "CAN", "NOT"]

var = []

def parse(lista_tokens):
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


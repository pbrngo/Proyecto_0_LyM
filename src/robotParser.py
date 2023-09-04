import re
import tokenizador as tok

NT = ["north", "south", "west", "east", "left", "right", "around", "front", "back",
    "DEFV", "DEFP", "{", "}", ";", "EQ", "O", "S", "V", "TURN", "ADV", "IF", "ELS",
    "WHL", "RPT", "TMS", "JMP", "WLK", "LP", "TRN", "DRP", "GET", "GRB", "LETGO", 
    "NOP", "TRNTO", "FCN", "CAN", "NOT"]

def parse(lista_tokens):
    x = 0
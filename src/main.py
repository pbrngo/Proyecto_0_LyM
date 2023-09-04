import tokenizador as tok
import robotParser as rp

print(rp.parse(tok.lexer("maquina-virtual.txt")))

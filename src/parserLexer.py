import nltk

variables = []
parametros = []
comandos = ["walk", "jump", "leap", "turn", "turnto", "drop", "grab", "get", "letGo", "nop"]
control_estructure = ["if", "while", "repeatTimes"]
condiciones = ["facing","can", "not"]
o = ["north", "south", "west", "east"]
d_min = ["front", "left", "right", "back"]
d_may = ["left", "right", "around"]
numero = ["0","1","2","3","4","5","6","7","8","9"]
vacio = []

def verificador(archivo_programa):
    """
    Este programa recibe el archivo de texto de un programa para un robot 
    y devuelve si es un programa valido o no.

    Parametros
        string: nombre del archivo de donde se sacara la informacion
    Return
        boolean: que representa si el archivo es valido o no
    """
    programa  = open(archivo_programa, 'r')
    esPrograma = True 
    #primera_linea = programa.readline()
    #ultima_linea = programa.readlines()[-1]
    linea = programa.readline()
    while(linea and esPrograma == True):
            if isVAR(linea) == False and linea != "\n":
                esPrograma = False
            elif isProcedureDefinition(linea, programa) == False and linea != "\n":
                esPrograma = False
            elif isInstructionBlock(programa) == False and linea != "\n":
                esPrograma = False
            else:
                linea = programa.readline()
    programa.close()
    return esPrograma

def isVAR(linea):
    """
    A variable definition starts with the keyword defVar followed by a name followed by an initial value.
    A procedure definition starts with the keyword defProc followed by by a name,
    followed by a list of parameter in parenthesis separated by commas, followed
    by a block of commands.
    """
    esVar = True
    linea = linea.split()
    if (linea[0] != "defvar"):
        esVar = False
    elif (numero != linea[-1][-1]):
        esVar = False
    else:
        for x in range(1, len(linea[1:]) + 1):
            try:
                variable = linea[x].replace(",", "")
                variable = variable.replace(";", "")
                variables.append(variable)
            except:
                esVar = False     
    return esVar

def isProcedureDefinition(linea, programa):
    """
    A procedure definition starts with the keyword defProc followed by by a name,
followed by a list of parameter in parenthesis separated by commas, followed
by a block of commands.
    """
    esPD = True
    tokenPROC = (linea.split())[0]

    #para encontrar los parametros
    ubicacionParentesis = linea.find("(")
    if tokenPROC != "defproc" or ubicacionParentesis == -1:
        esPD = False
    else:
        losParametros = linea[ubicacionParentesis:].replace("(", "").split()
        for para in losParametros:
            if para[-1] != "," and para[-1] != ")":
                esPD = False
                break
            else:
                p = para.replace(")", "")
                if p != "":
                    parametros.append(p)
        if not isInstructionBlock(programa):
            esPD = False
        
    return esPD

def isInstructionBlock(programa):
    """
    A block of commands is a sequence of commands separated by semicolons within
curly brackets
    """
    esIB = True
    abierto = True
    corchete = programa.readline()
    if corchete != "{":
        esIB = False
    else:
        while (abierto and esIB):
            linea = programa.readline()
            if (linea[0] == "}"):
                abierto = False
            elif linea == "\n":
                continue
            else:
                token = nltk.word_tokenize(linea.replace(", ", " "))
                if (token[0] == "defproc" or linea == "{") and abierto:
                    esIB = False
                elif isCommand(token) == False and linea != "\n":
                    esIB = False
                elif isControlStructure(token) == False and linea != "\n":
                    esIB = False
                else:
                    continue
    return True

def isCommand(token):
    """
    Verifica que un token sea un comando
    """
    esC = True
    if token[-1] != ";" and token[0] not in variables:
        esC = False
    else:
        if token[0] == "walk":
            if len(token) < 6:
                if (token[2] not in numero and token[2] not in variables and token[2] not in parametros):
                    esC = False
            elif len(token) == 6:
                if (token[3] not in numero and token[3] not in variables and token[3] not in parametros):
                    esC = False
                elif (token[2] not in o and token[2] not in d_min):
                    esC = False
            else:
                esC = False
        elif token[0] == "jump":
            if (token[2] not in numero and token[2] not in variables and token[2] not in parametros):
                    esC = False
        if token[0] == "leap":
            if len(token) < 6:
                if (token[2] not in numero and token[2] not in variables and token[2] not in parametros):
                    esC = False
            elif len(token) == 6:
                if (token[3] not in numero and token[3] not in variables and token[3] not in parametros):
                    esC = False
                elif (token[2] not in o and token[2] not in d_min):
                    esC = False
            else:
                isC = False
        elif token[0] == "turn":
            if token[2] not in d_may:
                    esC = False
        elif token[0] == "turnto":
            if token[2] not in o:
                esC = False
        elif token[0] == "drop":
            if token[2] not in numero:
                esC = False
        elif token[0] == "grab":
            if token[2] not in numero:
                esC = False
        elif token[0] == "get":
            if token[2] not in numero:
                esC = False
        elif token[0] == "letgo":
            if token[2] not in numero:
                esC = False
        elif token[0] == "nop":
            if token[2] not in vacio:
                esC = False
    
        else:
            if token[2] != ";=" and token[3] not in numero and token[1] not in variables:
                esC = False
    return esC

def isControlStructure(token):
    """
    Verifica que un token sea un Control Structure
    """
    esCD = True
    #if (condition){Block1} else {Block2} fi
    #if (condition){Block1} fi
    if token[0] == "if":
        con = token[2:(token.index(")", 2)) + 1]
        bloque1 = token[token.index("{") + 1 :token.index("}")]
        if isCondition(con) == False:
            esCD = False
        elif token.index("{") == -1 or token.index("}") == -1:
            esCD = False
        elif token[-1] != "fi":
            esCD == False
        elif isCommand(bloque1) == False:
            esCD = False
        else:
            if "else" in token:
                if token[token.index(")") + 1] != "else":
                    esCD = False
                else:
                    bloque2 = token[token.index("else") + 2 : token.index("}", token.index("else") + 1)]
                    if isCommand(bloque2) == False:
                        esCD = False
    elif token[0] == "while":
            con = token[2:(token.index(")", 2)) + 1]
            bloque1 = token[token.index("{") + 1 :token.index("}")]
            if isCondition(con) == False:
                esCD = False
            elif isCommand(bloque1) == False:
                esCD = False
    elif token[0] == "repeat" and token[2] == "times":
        if token[1] != numero:
            esCD = False
        else:
            bloque1 = token[token.index("{") + 1 :token.index("}")]
            if token[1] not in numero:
                esCD = False
            elif isCommand(bloque1) == False:
                esCD = False
    return esCD

def isCondition(token):
    """
    revisa si un token es una condicion
    """
    esCon = True
    if token[0] not in condiciones:
        esCon = False
    else:
        
        if token[0] == "facing":
            if token[2] not in o:
                esCon = False
        elif token[0] == "can":
            if (token[2] not in d_min and token[2] not in o) or (token[3] not in numero and token[3] not in variables and token[3] not in parametros):
                esCon = False
        elif token[0] == "not":
            condicion_valido = isCondition(token[2])
            if condicion_valido == False:
                esCon = False
    return esCon


print(verificador("maquina-virtual.txt"))

#print(verificador("\Users\ACER\Downloads\Proyecto_0_LyM-main\Proyecto_0_LyM-main\maquina-virtual.txt"))


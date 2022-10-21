# Written by George Lypopoulos cse84411 and Christos Brentas cse84442
# den kaftiaxame to file.c kai ton pinaka simbolon tha ta paradosoyme me ton teliko kodika

import sys

letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Add_operations = ['+', '-']

Mul_operations = ['*', '/']

correlation_operators = ['<', '>', '=', '<=', '>=', '<>']

assignment_symbol = ':='

separators = [';', ',']

grouping_symbols = ['[', ']', '(', ')', '{', '}']

program_termination = '.'

comments = '#'

committed_words = ['program', 'declare', 'if', 'else', 'while', 'switchcase', 'forcase', 'incase', 'case', 'default',
                   'not', 'and', 'or', 'function', 'procedure', 'call', 'return', 'in', 'inout', 'input', 'print']

leykoi_char = [' ', '\t']

entityList = {}
levelList = []
pinakasSimbolon = []

# arxikh katastash

start = 0

# endiameses katastaseis
dig = 1
idk = 2
asgn = 3
smaller = 4
larger = 5

# telikes katastaseis
number = 6
identifier = 7
keyword = 8
addOperator = 9
mulOperator = 10
groupSymbol = 11
delimiter = 12
assignment = 13
relOperator = 14

num_row = 1
num_coloumn = 0
flag = 0


def lex_anal():
    global num_row
    global num_coloumn
    global flag
    arxeio = open(sys.argv[1])

    torinh_katastash = start
    dhmioyrghmeno_token = ""

    for i in range(0, num_row, 1):
        grammh = arxeio.readline()

    if (flag == 1 and (grammh == "}." or "\n")):
        return "eof", "eof", line

    dhmioyrghmeno_token += grammh[num_coloumn]

    # Allagi Grammis sthn start
    while (dhmioyrghmeno_token == '\n'):
        num_row += 1
        num_coloumn = 0
        dhmioyrghmeno_token = ""
        grammh = arxeio.readline()
        dhmioyrghmeno_token += grammh[num_coloumn]

    # Leykos Xaraktiras sthn start
    while (dhmioyrghmeno_token in leykoi_char or dhmioyrghmeno_token == '\n'):
        if (dhmioyrghmeno_token != '\n'):
            num_coloumn += 1
            dhmioyrghmeno_token = ""
            dhmioyrghmeno_token += grammh[num_coloumn]
        else:
            num_row += 1
            num_coloumn = 0
            dhmioyrghmeno_token = ""
            grammh = arxeio.readline()
            dhmioyrghmeno_token += grammh[num_coloumn]

    # Sxolia
    if (dhmioyrghmeno_token == '#'):
        line_sxoliou = num_row
        dhmioyrghmeno_token = ''
        num_coloumn += 1
        # Oso einai mesa sta sxolia
        while (grammh[num_coloumn] != '#'):
            if (grammh[num_coloumn] == '\n'):
                num_row += 1
                grammh = arxeio.readline()
                num_coloumn = 0
            else:
                num_coloumn += 1
            if (grammh[num_coloumn] == '}.'):
                print("Lexical Error the arguments is not closed in line:", line_sxoliou)
                exit(1)
        num_coloumn += 1

        # An brei allagi grammis molis teliosoyn ta sxolia
        while (grammh[num_coloumn] == '\n'):
            num_row += 1
            num_coloumn = 0
            grammh = arxeio.readline()

        # An brei lefko xaraktira amesos meta ta sxolia
        while (grammh[num_coloumn] in leykoi_char):
            num_coloumn += 1
            dhmioyrghmeno_token = ""

        dhmioyrghmeno_token += grammh[num_coloumn]

    # Numbers katastash
    if (dhmioyrghmeno_token in numbers):
        torinh_katastash = dig;
        num_coloumn += 1
        while (grammh[num_coloumn] in numbers):
            dhmioyrghmeno_token += grammh[num_coloumn]
            num_coloumn += 1

        # Gramma meta apo arithmo
        if (grammh[num_coloumn] in letter):
            print("Lexical Error in line: ", num_row, 'Token :', dhmioyrghmeno_token)
            exit(1)

        # Ektos orion o akeraios
        if (int(dhmioyrghmeno_token) <= -(pow(2, 32) - 1) or int(dhmioyrghmeno_token) >= (pow(2, 32) - 1)):

            print("Lexical Error in line:", num_row, 'Integer token not allowed value:', dhmioyrghmeno_token)
            exit(1)

        # Fisiologiki katastash
        else:
            return int(dhmioyrghmeno_token), 'number', num_row

    # Letter katastash
    if (dhmioyrghmeno_token in letter):
        num_coloumn += 1
        while (grammh[num_coloumn] in letter or grammh[num_coloumn] in numbers):
            dhmioyrghmeno_token += grammh[num_coloumn]
            num_coloumn += 1

        # Megalo String
        if (len(dhmioyrghmeno_token) > 30):
            print("Lexical Error in line:", num_row, 'String length > 30:', dhmioyrghmeno_token)
            return "error", "EOT", num_row

        # Elegxos gia keyword/identifier
        else:
            if (dhmioyrghmeno_token in committed_words):
                return dhmioyrghmeno_token, "keyword", num_row

            else:
                return dhmioyrghmeno_token, "identifier", num_row

    # AddOperators katastash
    if (dhmioyrghmeno_token in Add_operations):
        num_coloumn += 1

        return dhmioyrghmeno_token, "addOperator", num_row

    # MulOperators katastash
    if (dhmioyrghmeno_token in Mul_operations):
        num_coloumn += 1

        return dhmioyrghmeno_token, "mulOperator", num_row

    # Delimiter katastash
    if (dhmioyrghmeno_token in separators):
        num_coloumn += 1

        return dhmioyrghmeno_token, "delimiter", num_row

    # Group Symbol
    if (dhmioyrghmeno_token in grouping_symbols):
        num_coloumn += 1

        return dhmioyrghmeno_token, "groupSymbol", num_row

    # Program_termination Symbol
    if (dhmioyrghmeno_token == program_termination):
        num_coloumn += 1
        flag = 1

        return dhmioyrghmeno_token, "Program_termination", num_row

    # Assignment_symbol
    if (dhmioyrghmeno_token == ':'):
        num_coloumn += 1
        if (grammh[num_coloumn] == '='):
            dhmioyrghmeno_token += grammh[num_coloumn]
            num_coloumn += 1
            return dhmioyrghmeno_token, "Assignment_symbol", num_row
        else:
            print("Lexical Error in line:", num_row, "After ':' there has to be '=' ")
            exit(-1)

    # Smaller symbol
    if (dhmioyrghmeno_token == '<'):
        num_coloumn += 1
        # sindiasmos me =
        if (grammh[num_coloumn] == '='):
            dhmioyrghmeno_token += grammh[num_coloumn]
            num_coloumn += 1
            return dhmioyrghmeno_token, "relOperator", num_row

        elif (grammh[num_coloumn] == '>'):
            dhmioyrghmeno_token += grammh[num_coloumn]
            num_coloumn += 1
            return dhmioyrghmeno_token, "relOperator", num_row
        else:

            return dhmioyrghmeno_token, "relOperator", num_row

    # Larger symbol
    if (dhmioyrghmeno_token == '>'):
        num_coloumn += 1

        # sindiasmos me =
        if (grammh[num_coloumn] == '='):
            dhmioyrghmeno_token += grammh[num_coloumn]
            num_coloumn += 1
            return dhmioyrghmeno_token, "relOperator", num_row

        else:

            return dhmioyrghmeno_token, "relOperator", num_row

    # Ison symbol
    if (dhmioyrghmeno_token == '='):
        num_coloumn += 1
        return dhmioyrghmeno_token, "relOperator", num_row



    # Ksenos xaraktiras
    else:
        print("Lexical Error in line:", num_row, "Unexpected Element ", dhmioyrghmeno_token)
        exit(1)


##############################################################################################################################################################

# PINAKAS SYMVOLWN#
global offset
global symbList
global argumentList
global symbList
symbList = []
global level
level = 0

argumentList = []
offset = 8


class Entity():
    def __init__(self, name):
        self.name = name

    class Variable:

        def __init__(self, name, datatype, offset):
            Entity.__init__(self, name)
            self.datatype = datatype
            self.offset = offset

        class TemporaryVariable:
            def __init__(self, name, datatype, offset):
                Entity.Variable.__init__(self, name, datatype, offset)

    class Procedure:
        def __init__(self, name, start_quad, frameLength, arguments_list):
            Entity.__init__(self, name)
            self.start_quad = start_quad
            self.frameLength = frameLength
            self.arguments_list = arguments_list

        class Function:
            def __init__(self, name, datatype, start_quad, frameLength, arguments_list):
                Entity.Procedure.__init__(self, name, start_quad, frameLength, arguments_list)
                self.datatype = datatype

    class FormalParameter:
        def __init__(self, name, datatype, mode):
            Entity.__init__(self, name)
            self.datatype = datatype
            self.mode = mode

        class Parameter:
            def __init__(self, datatype, mode, offset):
                Entity.Variable.__init__(self, datatype, mode, offset)

    class SymbolicConstant:
        def __init__(self, name, datatype, value):
            Entity.__init__(self, name)
            self.datatype = datatype
            self.value = value


class Scope:
    def __init__(self, level):
        self.level = level
        self.entityList = entityList


def addNewEntity(entity):
    global offset
    global pinakasSimbolon
    global level

    entityList[entity] = level - 1
    offset += 4

    if (type(entity) is Entity.Variable):
        pinakasSimbolon[len(pinakasSimbolon) - 1].append("Entity: " + entity.name + '/' + str(offset))

    elif (type(entity) is Entity.Procedure):
        pinakasSimbolon[len(pinakasSimbolon) - 1].append("Entity: " + entity.name + "/" + str(entity.frameLength))

    elif (type(entity) is Entity.Procedure.Function):
        pinakasSimbolon[len(pinakasSimbolon) - 1].append("Entity: " + entity.name + "/" + str(entity.frameLength))

    elif (type(entity) is Entity.FormalParameter):
        pinakasSimbolon[len(pinakasSimbolon) - 1].append("Entity: " + entity.name + "/" + entity.mode)


def addNewScope(name):
    global pinakasSimbolon
    global symbList
    global level

    pinakasSimbolon.append([level])
    symbList.append([])
    pinakasSimbolon[len(pinakasSimbolon) - 1].append("Scope: " + name + " Number  " + str(len(pinakasSimbolon) - 1))
    level += 1


def deleteLevel():
    global pinakasSimbolon
    global symbList

    symbList[pinakasSimbolon[-1][0]] = pinakasSimbolon[-1]
    if (pinakasSimbolon != []):
        pinakasSimbolon.pop(-1)


def updateFields(function, startingQuad, argList):
    global offset
    global argumentList
    if (type(function) == Entity.Procedure.Function):
        function.start_quad = startingQuad

    function.frameLength = offset + 4
    function.argumentList = argList

    return function.frameLength


def addTypParam(mode):
    global token
    global offset
    global argumentList

    entity = Entity.FormalParameter(token, 'int', mode)
    addNewEntity(entity)
    argumentList[-1].append(entity)


def symbFile():
    global pinakasSimbolon
    global symbList
    global entityList
    global argumentList

    symbfile = open("symbfile.symb", 'w+')

    for i in range(len(symbList)):
        for j in range(len(symbList[i])):
            symbfile.write(str(symbList[i][j]) + '\n')

    symbfile.close()


def search(nameEntity):
    global entityList
    list = []

    for i in entityList.keys():
        list.append(i)

    list.reverse()

    for i in range(0, len(list)):
        if (list[i].name == nameEntity):
            return list[i], entityList.get(list[i])

    print('H metablhth ' + nameEntity + ' den Brethike')
    exit(-1)


#############################################################################################################################################################


def synt_error():
    exit(1)


def varlist():
    global token, family, line
    global offset
    if (family == 'identifier'):
        entity = Entity.Variable(token, 'int', offset)
        addNewEntity(entity)
        token, family, line = lex_anal()
        while (token == ','):
            token, family, line = lex_anal()
            if (family == 'identifier'):
                entity = Entity.Variable(token, 'int', offset)
                addNewEntity(entity)
                token, family, line = lex_anal()

            else:
                synt_error()


def declarations():
    global token, family, line

    while (token == "declare"):
        token, family, line = lex_anal()
        varlist()

        if (token == ';'):
            token, family, line = lex_anal()

        else:
            print("Token: ", token, "Line: ", line)
            print("Invalid statement. Expected ';'.")
            synt_error()


def formalparitem():
    global token, family, line
    if (token == 'in' or token == 'inout'):
        if (token == 'in'):
            token, family, line = lex_anal()
            addTypParam('CV')

        else:
            token, family, line = lex_anal()
            addTypParam('REF')

        if (family == 'identifier'):
            token, family, line = lex_anal()


        else:
            print("Token: ", token, "Line: ", line)
            print("Invalid statement. Expected 'identifier'.")
            synt_error()

    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid statement. Expected 'in' or 'out'.")
        synt_error()


def formalparlist():
    global token, family, line
    token, family, line = lex_anal()
    if (token != ')'):
        formalparitem()

        while (token == ','):
            token, family, line = lex_anal()

            formalparitem()


def subprogram():
    global token, family, line
    global programSubName
    global offset
    global argumentList
    argumentList.append([])
    if (token == "function"):
        token, family, line = lex_anal()
        programSubName.append(token)

        if (family == 'identifier'):
            addNewScope(token)
            entity = Entity.Procedure.Function(token, 'int', 0, 0, [])
            token, family, line = lex_anal()

            if (token == '('):
                offset = 8
                formalparlist()

                if (token == ')'):
                    token, family, line = lex_anal()
                    startingQuad = block()
                    genQuad('end_block', programSubName[-1], "_", "_")
                    programSubName.pop(-1)

                else:
                    print("Token: ", token, "Line: ", line)
                    print("Wrong syntax. Expected ')'.")
                    synt_error()

            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected '('.")
                synt_error()

        else:
            print("Token: ", token, "Line: ", line)
            print("Invalid statement. Expected 'identifier'.")
            synt_error()
    elif (token == "procedure"):

        token, family, line = lex_anal()
        programSubName.append(token)

        if (family == 'identifier'):
            addNewScope(token)
            entity = Entity.Procedure(token, 0, 0, [])
            token, family, line = lex_anal()

            if (token == '('):
                offset = 8
                formalparlist()

                if (token == ')'):
                    token, family, line = lex_anal()
                    startingQuad = block()
                    genQuad('end_block', programSubName[-1], "_", "_")
                    programSubName.pop(-1)

                else:
                    print("Token: ", token, "Line: ", line)
                    print("Wrong syntax. Expected ')'.")
                    synt_error()

            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected '('.")
                synt_error()

        else:
            print("Token: ", token, "Line: ", line)
            print("Invalid statement. Expected 'identifier'.")
            synt_error()

    updateFields(entity, startingQuad, argumentList.pop(-1))
    deleteLevel()
    addNewEntity(entity)
    offset = len(pinakasSimbolon[-1] * 4) - 4


def subprograms():
    global token, family, line
    global programSubName
    while (token == 'function' or token == 'procedure'):
        subprogram()


def REL_OP():
    global token, family, line

    if (token == '='):
        token1 = token
        token, family, line = lex_anal()


    elif (token == '<='):
        token1 = token
        token, family, line = lex_anal()


    elif (token == '>='):
        token1 = token
        token, family, line = lex_anal()


    elif (token == '>'):
        token1 = token
        token, family, line = lex_anal()


    elif (token == '<'):
        token1 = token
        token, family, line = lex_anal()



    elif (token == '<>'):
        token1 = token
        token, family, line = lex_anal()


    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid argument.")
        synt_error()

    return token1


def ADD_OP():
    global token, family, line
    if (token == '+'):
        token, family, line = lex_anal()

    elif (token == '-'):
        token, family, line = lex_anal()


def optionalSign():
    global token, family, line
    ADD_OP()


def actualparitem():
    global token, family, line

    if (token == 'in'):
        token, family, line = lex_anal()
        expression()

    elif (token == 'inout'):
        token, family, line = lex_anal()
        expression()

    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid argument.")
        synt_error()


def actualparlist(src, id):
    global token, family, line

    if (token != ')'):
        actualparitem()
        while (token == ','):
            token, family, line = lex_anal()
            actualparitem()

        if (src == 'idtail'):
            nTemp = newTemp()
            genQuad('par', nTemp, 'ret', '_')
            genQuad('call', id, '_', '_')
            return nTemp


def idtail(id):
    global token, family, line
    idN = '_'
    src = 'idtail'
    if (token == '('):
        token, family, line = lex_anal()
        idN = actualparlist(src, id)

        if (token == ')'):
            token, family, line = lex_anal()
            newTemp1 = newTemp()
            genQuad('par', newTemp1, 'RET', '_')
            genQuad('call', id, '_', '_')

            return newTemp1



        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '('.")
            synt_error()


def factor():
    global token, family, line
    if (family == 'number'):
        number = token
        token, family, line = lex_anal()
        return number

    elif (token == '('):
        token, family, line = lex_anal()
        e = expression()
        if (token == ')'):
            token, family, line = lex_anal()
            f = e
            return f

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected ')'.")
            synt_error()

    elif (family == 'identifier'):
        token1 = token

        token, family, line = lex_anal()
        idreturn = idtail(token1)

        if (idreturn != None):
            return idreturn

        else:
            if (token1 not in variableList):
                variableList.append(token1)
            return token1

    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid argument.")
        synt_error()


def term():
    global token, family, line
    f = factor()
    while (token == '*' or token == '/'):
        telesths = token
        token, family, line = lex_anal()

        f2 = factor()
        w = newTemp()
        genQuad(telesths, f, f2, w)
        f = w
    t = f

    return t


def expression():
    global token, family, line
    optionalSign()
    t = term()
    while (token == '+' or token == '-'):
        telesths = token
        token, family, line = lex_anal()
        t2 = term()
        w = newTemp()
        genQuad(telesths, t, t2, w)
        t = w
    e = t

    return e


def boolfactor():
    global token, family, line
    rTrue = []
    rFalse = []
    if (token == 'not'):
        token, family, line = lex_anal()

        if (token == '['):
            token, family, line = lex_anal()
            b = condition()
            if (token == ']'):
                token, family, line = lex_anal()
                rFalse = b[1]
                rTrue = b[0]
                return rFalse, rTrue

            else:
                print("Wrong syntax. Expected ']'.")
                synt_error()

        else:
            print("Wrong syntax. Expected '['.")
            synt_error()

    elif (token == '['):
        token, family, line = lex_anal()
        b = condition()
        if (token == ']'):
            token, family, line = lex_anal()
            rFalse = b[0]
            rTrue = b[1]
            return rFalse, rTrue
        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected ']'.")
            synt_error()

    else:
        e1 = expression()
        telesths = REL_OP()
        e2 = expression()
        rTrue = makeList(nextQuad())
        genQuad(telesths, e1, e2, "_")
        rFalse = makeList(nextQuad())
        genQuad("jump", "_", "_", "_")

    return rFalse, rTrue


def boolterm():
    global token, family, line
    qFalse = []
    qTrue = []

    q = boolfactor()

    qFalse = q[0]
    qTrue = q[1]

    while (token == 'and'):
        backpatch(qTrue, nextQuad())
        token, family, line = lex_anal()
        r2 = boolfactor()
        qTrue = r2[1]
        qFalse = mergeList(qFalse, r2[0])

    return qFalse, qTrue


def statements():
    global token, family, line

    if (token == '{'):
        token, family, line = lex_anal()

        statement()
        while (token == ';'):
            token, family, line = lex_anal()
            statement()

        if (token == '}'):
            token, family, line = lex_anal()


        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '{'.")
            synt_error()
    else:
        statement()
        if (token == ';'):

            token, family, line = lex_anal()
        else:
            print("Token: ", token, "Line: ", line)
            print("Invalid argument.")
            synt_error()


def condition():
    global token, family, line
    bTrue = []
    bFalse = []

    q1 = boolterm()
    bFalse = q1[0]
    bTrue = q1[1]
    while (token == 'or'):
        backpatch(bFalse, nextQuad())
        token, family, line = lex_anal()
        q2 = boolterm()
        bFalse = q2[0]
        bTrue = mergeList(bTrue, q2[1])

    return bFalse, bTrue


def inputStat():
    global token, family, line
    token, family, line = lex_anal()

    if (token == '('):
        token, family, line = lex_anal()

        if (family == 'identifier'):
            genQuad('in', token, '_', '_')
            token, family, line = lex_anal()

            if (token == ')'):
                token, family, line = lex_anal()

            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected ')'.")
                synt_error()
        else:
            print("Token: ", token, "Line: ", line)
            print("Invalid statement. Expected 'identifier'.")
            synt_error()

    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected '('.")
        synt_error()


def printStat():
    global token, family, line
    token, family, line = lex_anal()

    if (token == '('):
        token, family, line = lex_anal()
        exp = expression()
        genQuad('out', exp, '_', '_')
        if (token == ')'):

            token, family, line = lex_anal()

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected ')'.")
            synt_error()

    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected '('.")
        synt_error()


def callStat():
    global token, family, line
    token, family, line = lex_anal()
    name = token
    if (family == 'identifier'):
        token, family, line = lex_anal()

        if (token == '('):
            token, family, line = lex_anal()
            actualparlist('idtail', token)
            genQuad('call', name, '_', '_')

            if (token == ')'):
                token, family, line = lex_anal()

            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected ')'.")
                synt_error()
        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '('.")
            synt_error()

    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid argument. Expected 'identifier'.")
        synt_error()


def returnStat():
    global token, family, line
    token, family, line = lex_anal()

    if (token == '('):
        token, family, line = lex_anal()
        exp = expression()
        genQuad('ret', exp, '_', '_')

        if (token == ')'):
            token, family, line = lex_anal()


        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected ')'.")
            synt_error()

    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected '('.")
        synt_error()


def incaseStat():
    global token, family, line
    token, family, line = lex_anal()
    while (token == 'case'):

        token, family, line = lex_anal()
        if (token == '('):
            token, family, line = lex_anal()
            condition()
            if (token == ')'):
                token, family, line = lex_anal()
                statements()

            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected ')'.")
                synt_error()

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '('.")
            synt_error()


def forcaseStat():
    global token, family, line
    token, family, line = lex_anal()
    while (token == 'case'):
        token, family, line = lex_anal()
        if (token == '('):
            token, family, line = lex_anal()
            condition()
            if (token == ')'):
                token, family, line = lex_anal()
                statements()
            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected ')'.")
                synt_error()

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '('.")
            synt_error()

    if (token == 'default'):
        token, family, line = lex_anal()
        statements()

    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid argument. Expected 'default'.")
        synt_error()


def switchcaseStat():
    global token, family, line
    switchTrue = []
    switchFalse = []
    exit = emptyList()

    token, family, line = lex_anal()
    while (token == 'case'):
        token, family, line = lex_anal()
        if (token == '('):
            token, family, line = lex_anal()
            cList = condition()
            switchTrue = cList[1]
            switchFalse = cList[0]

            if (token == ')'):
                backpatch(switchTrue, nextQuad())
                token, family, line = lex_anal()
                statements()
                l = makeList(nextQuad())
                genQuad('jump', '_', '_', '_')
                exit = mergeList(exit, l)
                backpatch(switchFalse, nextQuad())


            else:
                print("Token: ", token, "Line: ", line)
                print("Wrong syntax. Expected ')'.")
                synt_error()

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '('.")
            synt_error()

    if (token == 'default'):
        token, family, line = lex_anal()
        statements()
        backpatch(exit, nextQuad())

    else:
        print("Token: ", token, "Line: ", line)
        print("Invalid argument. Expected 'default'.")
        synt_error()


def whileStat():
    global token, family, line
    whileFalse = []
    whileTrue = []
    whilequad = nextQuad()
    token, family, line = lex_anal()

    if (token == '('):
        token, family, line = lex_anal()
        c = condition()
        whileTrue = c[1]
        whileFalse = c[0]
        if (token == ')'):
            backpatch(whileTrue, nextQuad())

            token, family, line = lex_anal()
            statements()
            genQuad('jump', '_', '_', whilequad)
            backpatch(whileFalse, nextQuad())


        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected ')'.")
            synt_error()
    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected '('.")
        synt_error()


def elsepart():
    global token, family, line
    if (token == 'else'):
        token, family, line = lex_anal()
        statements()


def ifStat():
    global token, family, line
    ifTrue = []
    ifFalse = []
    ifList = []
    token, family, line = lex_anal()
    if (token == '('):
        token, family, line = lex_anal()
        c = condition()
        ifFalse = c[0]
        ifTrue = c[1]
        if (token == ')'):
            backpatch(ifTrue, nextQuad())

            token, family, line = lex_anal()
            statements()
            ifList = makeList(nextQuad())
            genQuad('jump', '_', '_', '_')
            backpatch(ifFalse, nextQuad())

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected ')'.")
            synt_error()

        elsepart()
        backpatch(ifList, nextQuad())
    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected '('.")
        synt_error()


def assignStat():
    global token, family, line
    global variableList
    id = token
    if (token not in variableList):
        variableList.append(token)
    token, family, line = lex_anal()

    if (token == ':='):
        token, family, line = lex_anal()
        t = expression()
        genQuad(':=', t, "_", id)


    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected ':='.")
        synt_error()


def statement():
    global token, family, line

    if (family == 'identifier'):
        assignStat()
    elif (token == 'if'):
        ifStat()
    elif (token == 'while'):
        whileStat()
    elif (token == 'switchcase'):
        switchcaseStat()
    elif (token == 'forcase'):
        forcaseStat()
    elif (token == 'incase'):
        incaseStat()
    elif (token == 'call'):
        callStat()
    elif (token == 'return'):
        returnStat()
    elif (token == 'input'):
        inputStat()
    elif (token == 'print'):
        printStat()


def blockstatements():
    global token, family, line
    global programSubName
    startingQuad = nextQuad() + 2
    genQuad("begin_block", programSubName[-1], "_", "_")
    statement()
    while (token == ";"):
        token, family, line = lex_anal()
        statement()

    return startingQuad


def block():
    global token, family, line
    global startingQuad

    if (token == '{'):
        token, family, line = lex_anal()
        declarations()
        subprograms()
        startingQuad = blockstatements()

        if (token == '}'):
            token, family, line = lex_anal()
            telikosKodika()

        else:
            print("Token: ", token, "Line: ", line)
            print("Wrong syntax. Expected '}'.")
            synt_error()


    else:
        print("Token: ", token, "Line: ", line)
        print("Wrong syntax. Expected '{'.")
        synt_error()

    return startingQuad


def program():
    global level
    global onomaArxeioy
    global telikosKodikas
    flagfullstop = False
    global token, family, line
    global programSubName
    if (token == 'program'):
        token, family, line = lex_anal()
        addNewScope(token)

        if (family == 'identifier'):
            onomaArxeioy = 'main_' + token
            programSubName.append('main_' + token)
            token, family, line = lex_anal()
            block()

            if (token == '.'):

                deleteLevel()

                genQuad('halt', '_', '_', '_')
                genQuad('end block', programSubName[-1], '_', '_')
                programSubName.pop(-1)



                token, family, line = lex_anal()

                if (token == "eof"):
                    print("")


                else:
                    synt_error()

            else:
                print("Every program should end with a fullstop, fullstop at the end is missing")
                synt_error()

        else:
            print("Token: ", token, "Line: ", line)
            print('Expected a name for the program but found "keyword".')
            synt_error()

    else:
        print("Token: ", token, "Line: ", line)
        print("All programs should start with the keyword “program”. Ιnstead, the word", " '", token, "'", " appeared.")
        synt_error()


def synt_anal():
    global token, family, line
    token, family, line = lex_anal()

    program()
    print('compilation successfully completed')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global programSubName
programSubName = []
global quads
quads = 0
quadriples = []
global tempVarPointer
tempVarPointer = 0
global tList
tList = []
global variableList
variableList = []


def genQuad(operator, operand1, operand2, operand3):
    global quads
    tempList = [quads, operator, operand1, operand2, operand3]
    quads += 1
    quadriples.append(tempList)


def nextQuad():
    return quads


def newTemp():
    global tempVarPointer
    global offset
    tempVarPointer += 1
    x = 'T_' + str(tempVarPointer)
    tList.append(x)
    entity = Entity.Variable(x, 'int', offset)
    addNewEntity(entity)
    return x


def emptyList():
    tempList = []
    return tempList


def makeList(label):
    templist = [label]
    return templist


def mergeList(list1, list2):
    finalList = []
    finalList = list1 + list2

    return finalList


def backpatch(list, label):
    global quadriples
    for i in list:
        quadriples[i][4] = label


name = "endiamsesos"


def int_file():
    file = name + '.int'
    intfile = open(file, 'w+')

    for i in range(len(quadriples)):
        intfile.write(str(quadriples[i][0]))
        intfile.write(': ')
        intfile.write(str(quadriples[i][1]))
        intfile.write(' ')
        intfile.write(str(quadriples[i][2]))
        intfile.write(' ')
        intfile.write(str(quadriples[i][3]))
        intfile.write(' ')
        intfile.write(str(quadriples[i][4]))
        intfile.write(' ')
        intfile.write('\n')

    intfile.close()


def cfile():
    print(tList)
    file = name + ".c"
    filec = open(file, 'w+')

    filec.write("include <stdio.h>\n\n")
    filec.write("int main(){\n")

    if (len(tList) != 0):
        filec.write("\tint  ")
    for i in range(len(tList)):
        filec.write(tList[i])
        if (len(tList) == i + 1):
            filec.write(';')
            filec.write('\n')
        else:
            filec.write(',')

    if (len(variableList) != 0):
        filec.write("\tint ")
        for i in range(len(variableList)):
            filec.write(variableList[i])
            if (len(variableList) == i + 1):
                filec.write(';')
                filec.write('\n')
            else:
                filec.write(',')

    for j in range(len(quadriples)):
        if (quadriples[j][1] == 'begin_block'):
            filec.write('L_' + str(j) + ':' + '\n\t')
        elif (quadriples[j][1] == '+'):
            filec.write(
                'L_' + str(j) + ': ' + str(quadriples[j][4]) + '=' + str(quadriples[j][2]) + '+' + str(
                    quadriples[j][3]) + ';\n\t')
        elif (quadriples[j][1] == '-'):
            filec.write(
                'L_' + str(j) + ': ' + str(quadriples[j][4]) + '=' + str(quadriples[j][2]) + '-' + str(
                    quadriples[j][
                        3]) + ';\n\t')
        elif (quadriples[j][1] == '*'):
            filec.write(
                'L_' + str(j) + ': ' + str(quadriples[j][4]) + '=' + str(quadriples[j][2]) + '*' + str(
                    quadriples[j][3]) + ';\n\t')
        elif (quadriples[j][1] == '/'):
            filec.write(
                'L_' + str(j) + ': ' + str(quadriples[j][4]) + '=' + str(quadriples[j][2]) + '/' + str(
                    quadriples[j][3]) + ';\n\t')
        elif (quadriples[j][1] == '>'):
            filec.write(
                'L_' + str(j) + ': ' + 'if (' + str(quadriples[j][2]) + '>' + str(
                    quadriples[j][3]) + ') goto L_' + str(
                    str(quadriples[j][4])) + ';\n\t')
        elif (quadriples[j][1] == '>='):
            filec.write(
                'L_' + str(j) + ': ' + 'if (' + str(quadriples[j][2]) + '>=' + str(
                    quadriples[j][3]) + ') goto L_' + str(quadriples[j][4]) + ';\n\t')
        elif (quadriples[j][1] == '<'):
            filec.write(
                'L_' + str(j) + ': ' + 'if (' + str(str(quadriples[j][2])) + '<' + str(
                    str(quadriples[j][3])) + ') goto L_' + str(
                    str(quadriples[j][4])) + ';\n\t')
        elif (quadriples[j][1] == '<='):
            filec.write(
                'L_' + str(j) + ': ' + 'if (' + str(quadriples[j][2]) + '<=' + str(
                    quadriples[j][3]) + ') goto L_' + str(
                    str(quadriples[j][4])) + ';\n\t')
        elif (quadriples[j][1] == '<>'):
            filec.write(
                'L_' + str(j) + ': ' + 'if (' + str(quadriples[j][2]) + '<>' + str(
                    quadriples[j][3]) + ') goto L_' + str(
                    str(quadriples[j][4])) + ';\n\t')
        elif (quadriples[j][1] == '='):
            filec.write(
                'L_' + str(j) + ': ' + 'if (' + str(quadriples[j][2]) + '==' + str(
                    quadriples[j][3]) + ') goto L_' + str(
                    str(quadriples[j][4])) + ';\n\t')
        elif (quadriples[j][1] == ':='):
            filec.write(
                'L_' + str(j) + ': ' + str(str(quadriples[j][4])) + '=' + str(str(quadriples[j][2])) + ';\n\t')
        elif (quadriples[j][1] == 'in'):
            filec.write('L_' + str(j) + ': ' + 'scanf(\'%d\',&' + str(quadriples[j][2]) + ');\n\t')
        elif (quadriples[j][1] == 'out'):
            filec.write(
                "L_" + str(j) + ": " + "printf(\"" + " %d\", " + str(str(quadriples[j][2])) + ");\n\t")
        elif (quadriples[j][1] == 'jump'):
            filec.write("L_" + str(j) + ": " + "goto L_" + str(str(quadriples[j][4])) + ";\n\t")
        elif (quadriples[j][1] == 'halt'):
            filec.write("L_" + str(j) + ": {}\n")

    filec.write("\t exit(-1)")
    filec.write("\n}")



##################################################################################################################################################################################################
################################################################ TELIKOS KODIKAS ##################################################################################################################


def gnvlCode(nameEntity):
    global level
    global telikosKodikas
    entity, level1 = search(nameEntity)
    diff = level - level1
    telikosKodikas.write("lw $t0,-4($sp)\n")
    for i in range(1, diff):
        telikosKodikas.write("lw $t0,-4($t0)\n")

    telikosKodikas.write("addi $t0,$t0," + "-" + str(entity.offset) + "\n")


def loadvr(nameEntity, reg):
    global level

    if (isinstance(nameEntity, int)):
        telikosKodikas.write((f'li {reg}, {nameEntity}\n'))
    else:
        v, level1 = search(nameEntity)
        if (level1 == 0):
            if (v == Entity.Variable):
                telikosKodikas.write((f'lw {reg}, -{v.offset}($gp)\n'))

        if (level == level1):
            if (v == Entity.Variable.TemporaryVariable or v == Entity.Variable or (
                    v == Entity.FormalParameter and v.mode == "CV")):
                telikosKodikas.write(f'lw {reg}, -{v.offset}($sp)')

            elif (v == Entity.FormalParameter and v.mode == 'REF'):
                telikosKodikas.write(f'lw ($t0), -{v.offset}($sp)\n')
                telikosKodikas.write(f'lw {reg}, ($t0)\n')

        elif (level > level1):
            if (v == Entity.Variable or (v == Entity.FormalParameter and v.mode == 'CV')):
                gnvlCode(nameEntity)
                telikosKodikas.write(f'lw {reg}, ($t0)\n')

            elif (v == Entity.FormalParameter and v.mode == "REF"):
                gnvlCode(nameEntity)
                telikosKodikas.write(f'lw $t0, ($t0)\n')
                telikosKodikas.write(f'lw {reg}, ($t0)\n')


def storerv(reg, entityName):
    global level
    global telikosKodikas
    entity, level1 = search(entityName)

    if (level == 0 and entity == Entity.Variable):
        telikosKodikas.write(f'sw {reg}, -{entity.offset}($gp)\n')

    elif (level1 == level):
        if (entity == Entity.Variable.TemporaryVariable or entity == Entity.Variable or (
                entity == Entity.FormalParameter and entity.mode == "CV")):
            telikosKodikas.write(f'sw {reg}, -{entity.offset}($sp)\n')

        elif (entity == Entity.FormalParameter and entity.mode == "REF"):
            telikosKodikas.write(f'lw $t0, -{entity.offset}($sp)\n'
                                 f'sw {reg}, ($t0)\n')

    elif (level > level1):
        if (entity == Entity.Variable or (entity == Entity.FormalParameter and entity.mode == "CV")):
            gnvlCode(entityName)
            telikosKodikas.write(f'sw {reg}, ($t0)\n')
        elif (entity == Entity.FormalParameter and entity.mode == "REF"):
            gnvlCode()
            telikosKodikas.write(f'sw {reg}, ($t0)\n')


def telikosKodika():
    global quadriples
    global onomaArxeioy
    global telikosKodikas
    global level
    framelength = 8
    numParameters = 0
    grammh = 0

    for i in range(len(quadriples)):
        print(quadriples[i][0], quadriples[i][1], quadriples[i][2], quadriples[i][3], quadriples[i][4])
        if (quadriples[i][1] == 'begin_block'):
                telikosKodikas.write(f'L {quadriples[i][2]}:\n')


        if (quadriples[i][1] == "RET"):
            loadvr(quadriples[i][2], '$t1')
            telikosKodikas.write('lw $t0, -8($sp)\n'
                                 'sw $t1,($t0)\n')


        elif (quadriples[i][1] == "jump"):
            telikosKodikas.write(f'b {quadriples[i][4]}\n')


        elif (quadriples[i][1] == ":="):
            loadvr(quadriples[i][2], '$t1')
            storerv('$t1', quadriples[i][4])



        elif quadriples[i][1] in correlation_operators:
            loadvr(quadriples[i][2], '$t1')
            loadvr(quadriples[i][3], '$t2')
            if quadriples[i][1] == '=':
                telikosKodikas.write(f'beq $t1, $t2, {quadriples[i][3]}\n')
            elif quadriples[i][1] == '<>':
                telikosKodikas.write(f'bne $t1, $t2, {quadriples[i][3]}\n')
            elif quadriples[i][1] == '<':
                telikosKodikas.write(f'blt $t1, $t2, {quadriples[i][3]}\n')
            elif quadriples[i][1] == '<=':
                telikosKodikas.write(f'bge $t1, $t2, {quadriples[i][3]}\n')
            elif quadriples[i][1] == '>=':
                telikosKodikas.write(f'ble $t1, $t2, {quadriples[i][3]}\n')

            elif (quadriples[i][1] == '>'):
                telikosKodikas.write('bgt t1,t2,' + str(quadriples[i][3]) + '\n')


        elif (quadriples[i][1] in Add_operations or quadriples[i][1] in Mul_operations):
            loadvr(quadriples[i][2], '$t1')
            loadvr(quadriples[i][2], '$t2')
            if quadriples[i][1] == '+':
                telikosKodikas.write('add $t1, $t1, $t2\n')
            if quadriples[i][1] == '-':
                telikosKodikas.write('sub $t1, $t1, $t2\n')
            if quadriples[i][1] == '*':
                telikosKodikas.write('mul $t1, $t1, $t2\n')
            if quadriples[i][1] == '/':
                telikosKodikas.write('div $t1, $t1, $t2\n')
            storerv('$t1', quadriples[i][4])

        elif (quadriples[i][3] == "REF"):
            v, level1 = search(quadriples[i][2])
            diff = level - level1

            if (diff == 0):
                if (v == Entity.FormalParameter and v.mode == "CV"):
                    telikosKodikas.write(f'addi $t0, $sp, -{v.offset}\n '
                                         f'sw $t0, -{12 + 4 * numParameters}($fp)\n')
                    numParameters += 1

                elif (v == Entity.FormalParameter and v.mode == "REF"):
                    telikosKodikas.write(f'lw $t0, -{v.offset}\n '
                                         f'sw $t0, -{12 + 4 * numParameters}($fp)\n')
                    numParameters += 1

                elif (v == Entity.FormalParameter and v.mode == "REF"):
                    gnvlCode(quadriples[i][2])
                    telikosKodikas.write(f'lw $t0, ($t0)\n '
                                         f'sw $t0, -{12 + 4 * numParameters}($fp)\n')
                    numParameters += 1

                elif (diff != 0):
                    if (v == Entity.FormalParameter and v.mode == "CV"):
                        gnvlCode(quadriples[i][2])
                        telikosKodikas.write(f'sw $t0, -{12 + 4 * numParameters}($fp)\n')
                        numParameters += 1




            elif (quadriples[i][1] == 'call'):

                v, level1 = search(quadriples[1][4])

                diff = level - level1
                if diff == 0:
                    telikosKodikas.write('lw $t0, -4($sp)\n '
                                         'sw $t0, -4($fp)\n')
                else:
                    telikosKodikas.write('sw $sp, -4($fp)\n')
                telikosKodikas.write(
                    f'addi $sp, $sp, {v.frameLength}\n jal {quadriples[i][4]}\n '
                    f'addi $sp, $sp, -{v.framelength}\n')

        if quadriples[i][1] == 'begin_block':
            if quadriples[i][2] == 'main':
                for i in entityList:
                    if i.level == 0:
                        framelength += 4
                telikosKodikas.write(f'addi $sp, $sp, {framelength}\n '
                                     f'move $gp, $sp\n')
            else:
                telikosKodikas.write('sw $ra, -0($sp)\n')
        if quadriples[i][1] == 'end_block':
            telikosKodikas.write('lw $ra, -0($sp)\n'
                                 'jr $ra\n')
        if quadriples[i][1] == 'out':
            entity = search(quadriples[i][2])
            telikosKodikas.write(f'lw $t1, -($sp)')

file = 'telikoskodika.asm'
telikosKodikas = open(file, "w+")
synt_anal()
int_file()
cfile()
print(variableList)
symbFile()

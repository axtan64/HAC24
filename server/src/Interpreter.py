#2D array that stores an array containing the name of a variable and its value
variables = []
#Determines whether the code should be interpreted or not
run = True
#The code itself
lines = []
#Previous line of code ran
prevLine = ""
#How many loops are left
forStack = []
#Current while loop pointers
whileStack = []

#Gets the lines of code from a file
def getLines(text):
    global lines
    lines = text.split("\n")
    return lines

#Main algorithm
def interpret(text):
    global lines,pointer, prevLine
    try:
        pointer = 0
        #Get lines of code from string
        lines = getLines(text)
        #Check every line in the file
        while run == True:
            line = lines[pointer]
            currentLine = line
            #Checks for each syntax
            if "CREATE" in line:
                name = line.replace("CREATE", "")
                createVariable(name)
            elif "SET" in line and "TO" in line:
                first = line.find("SET")
                second = line.find("TO")
                name = line[first+3 : second]
                value = line[second+2 : len(line)]
                setVariable(name, value)
            elif "SUBMIT" in line:
                name = line.replace("SUBMIT", "")
                name = name.lower()
                return submit(name)
            elif "ADD" in line and "TO" in line:
                first = line.find("ADD")
                second = line.find("TO")
                value = line[first+3 : second]
                name = line[second+2 : len(line)]
                add(name, value)
            elif "SUBTRACT" in line and "FROM" in line:
                first = line.find("SUBTRACT")
                second = line.find("FROM")
                value = line[first+8 : second]
                name = line[second+4 : len(line)]
                subtract(name, value)
            elif "MULTIPLY" in line and "BY" in line:
                first = line.find("MULTIPLY")
                second = line.find("BY")
                name = line[first+8 : second]
                value = line[second+2 : len(line)]
                multiply(name, value)
            elif "DIVIDE" in line and "BY" in line:
                first = line.find("DIVIDE")
                second = line.find("BY")
                name = line[first+6 : second]
                value = line[second+2 : len(line)]
                divide(name, value)
            elif "IF" in line and "THEN" in line:
                line = line.replace("IF", "")
                line = line.replace("THEN", "")
                ifStatement(line)
            elif "ELSE" == line:
                elseStatement()
            elif "FOR" in line and "MANYTIMES" in line:
                line = line.replace("FOR", "")
                line = line.replace("MANYTIMES", "")
                forStatement(line)
            elif "ENDFOR" == line:
                endForStatement()
            elif "WHILE" in line and "ISTRUE" in line:
                line = line.replace("WHILE", "").replace("ISTRUE", "")
                whileStatement(line)
            elif "ENDWHILE" == line:
                endWhileStatement()
            prevLine = currentLine
            pointer += 1
    except:
        throwError("Syntax error present")


#Subroutine to create a new variable, initialised to zero
def createVariable(name):
    if name.islower() ==  False:
        throwError("Invalid Variable Name")
    for variable in variables:
        if variable[0] == name:
            throwError("Variable already exists")
            break
    variables.append([name, 0])

#Sets a variable to a corresponding value
def setVariable(name, value):
    for i in range(len(variables)):
        if variables[i][0] == name:
            variables[i][1] = int(value)

#Gets the value of a variable
def getVariable(name):
    for i in range(len(variables)):
        if variables[i][0] == name:
            return variables[i][1]

#Returns the corresponding variable value
def submit(variable):
    return getVariable(variable)

#Adds a value/variable to a variable
def add(name, value):
    end = False
    for i in range(len(variables)):
        if variables[i][0] == name:
            for j in range(len(variables)):
                if variables[j][0] == value:
                    variables[i][1] += variables[j][1]
                    end = True
                    break
            if end == False:
                variables[i][1] += int(value)
            break

#Subtracts a variable/value from another variable
def subtract(name, value):
    end = False
    for i in range(len(variables)):
        if variables[i][0] == name:
            for j in range(len(variables)):
                if variables[j][0] == value:
                    variables[i][1] -= variables[j][1]
                    end = True
                    break
            if end == False:
                variables[i][1] -= int(value)
            break

#Multiplies a variable by a value/variable
def multiply(name, value):
    end = False
    for i in range(len(variables)):
        if variables[i][0] == name:
            for j in range(len(variables)):
                if variables[j][0] == value:
                    variables[i][1] *= variables[j][1]
                    end = True
                    break
            if end == False:
                variables[i][1] *= int(value)
            break

#Divides a variable by a value/variable
def divide(name, value):
    end = False
    for i in range(len(variables)):
        if variables[i][0] == name:
            for j in range(len(variables)):
                if variables[j][0] == value:
                    variables[i][1] /= variables[j][1]
                    end = True
                    break
            if end == False:
                variables[i][1] /= int(value)
            break

#Checks if statement conditions
def ifStatement(condition):
    global lines,pointer
    for i in range(len(variables)):
        if variables[i][0] in condition:
            condition = condition.replace(variables[i][0], str(variables[i][1]))
    if eval(condition):
        pass
    else:
        noOfIfs = 0
        for i in range(len(lines)-1):
            if i>pointer:
                if (lines[i] == "ENDIF" or lines[i] == "ELSE") and noOfIfs == 0:
                    pointer = i
                    break
                elif lines[i] == "ENDIF" or lines[i] == "ELSE":
                    noOfIfs -= 1
                elif "IF" in lines[i] and "THEN" in lines[i]:
                    noOfIfs += 1

#Checks else statement conditions
def elseStatement():
    global lines,pointer, prevLine
    if not ("IF" in prevLine and "THEN" in prevLine):
        noOfIfs = 0
        for i in range(len(lines)-1):
            if i>pointer:
                if lines[i] == "ENDIF" and noOfIfs == 0:
                    pointer = i
                elif lines[i] == "ENDIF":
                    noOfIfs -= 1
                elif "IF" in lines[i] and "THEN" in lines[i]:
                    noOfIfs += 1
    else:
        condition = prevLine.replace("IF", "").replace("THEN", "")
        for i in range(len(variables)):
            if variables[i][0] in condition:
                condition = condition.replace(variables[i][0], str(variables[i][1]))
        if not eval(condition):
            pass
        else:
            noOfIfs = 0
            for i in range(len(lines)-1):
                if i>pointer:
                    if lines[i] == "ENDIF" and noOfIfs == 0:
                        pointer = i
                    elif lines[i] == "ENDIF":
                        noOfIfs -= 1
                    elif "IF" in lines[i] and "THEN" in lines[i]:
                        noOfIfs += 1

#Controls how many times a loop is run
def forStatement(n):
    global pointer, forStack
    for i in range(len(variables)-1):
        if variables[i][0] == n:
            n = variables[i][1]
    forStack.append([pointer, int(n)])

#Called when the end of a loop is reached, either restarts loop or stops it depending on counter
def endForStatement():
    global pointer, forStack
    forStack[len(forStack)-1][1] -= 1
    if forStack[len(forStack)-1][1] == 0:
        forStack.pop(len(forStack)-1)
        pass
    else:
        pointer = forStack[len(forStack)-1][0]

#Called when iterating with a while loop
def whileStatement(condition):
    global pointer
    for i in range(len(variables)):
        if variables[i][0] in condition:
            condition = condition.replace(variables[i][0], str(variables[i][1]))
    if eval(condition):
        whileStack.append(pointer)
    else:
        noOfWhiles = 0
        for i in range(len(lines) - 1):
            if i > pointer:
                if lines[i] == "ENDWHILE" and noOfWhiles == 0:
                    pointer = i
                    break
                elif lines[i] == "ENDWHILE":
                    noOfWhiles -= 1
                elif "WHILE" in lines[i] and "ISTRUE" in lines[i]:
                    noOfWhiles += 1

#Marks the end of a while statement, either iterates back or continues on
def endWhileStatement():
    global pointer
    pointer = whileStack[len(whileStack)-1]-1
    whileStack.pop(len(whileStack)-1)

#Called when an error occurs
def throwError(message):
    global run
    print(message)
    run = False





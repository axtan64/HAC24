def fixString(text):
    text = text.replace("=;", "=")
    text = text.replace(" ", "")
    text.replace("True;", "")
    text.replace("False;", "")
    text = text.split(";")
    return text

def convertToGraph(lis):
    #Example: [A, [B, C]] where A is the node and B and C is its children
    lis = fixString("a=10;b=20;a<b?;b=;b-a;a=;a-b;submit b; submit a")
    converting = True
    pointer = 0
    noOfDecisions = 0
    graph = []
    while converting:
        if "?" in lis[pointer]:
            graph.append([lis[pointer], [lis[pointer+1+noOfDecisions], lis[pointer+2+noOfDecisions]]    ])
            noOfDecisions += 1
        pointer += noOfDecisions



def getTree(text):
    lines = fixString("None;a=10;b=20;a<b?;b=;b-a;a=;a-b;submit b; submit a")
    newlines = fixString("None; a=10")
    run = True
    linePointer = 1
    pointer = 1
    while run == True:
        if None != newlines[pointer] and "?" not in newlines[pointer]:
            temp = pointer
            pointer = (pointer*2)+1
            if linePointer < len(lines)-1:
                linePointer = linePointer+1
                newlines.insert(pointer -1,lines[linePointer])
                newlines.insert(pointer, None)
                pointer = temp
            else:
                run = False
        elif newlines[pointer] == None:
            newlines.insert((pointer * 2) + 1, None)
            newlines.insert((pointer * 2), None)
        else:
            linePointer += 1
            temp = pointer
            pointer = pointer*2
            pointer
            newlines.insert(pointer, lines[linePointer])
            linePointer += 1
            newlines.insert(pointer, lines[linePointer])
            pointer = temp
        if len(lines)-1 > 2**10:
            run = False
        pointer += 1
    #newlines.pop(0)
    return newlines

#Perform a depth first traversal, once the item is found, return the stack of commands that leads to it
def depthFistSearch(lis, item, depthpointer):
    if depthpointer*2+1 >= len(lis):
        if lis[depthpointer] == item:
            depthStack.append(lis[depthpointer])
            return depthStack
    if len(depthStack) != 0 and depthStack[len(depthStack)-1] == lis[depthpointer]:
        pass
    else:
        if visited[depthpointer] == False:
            depthStack.append(lis[depthpointer])
    visited[depthpointer] = True
    if lis[depthpointer] == item:
        return depthStack
    while depthpointer*2 > len(lis)-1:
        depthStack.pop()
        if depthpointer%2==0:
            return depthFistSearch(lis, item, int(depthpointer/2))
        else:
            return depthFistSearch(lis, item, int((depthpointer-1)/2))
    if depthpointer > len(lis):
        pass
    else:
        if not visited[depthpointer*2]:
            return depthFistSearch(lis, item , depthpointer*2)
        if not visited[depthpointer*2+1]:
            return depthFistSearch(lis, item, int((depthpointer*2)+1))
        else:
            depthStack.pop()
            depthFistSearch(lis, item, int(depthpointer/2))
        for state in visited:
            if state == True:
                pass
            else:
                break
            return -1
        return depthStack


def doInstructions(array):
    variables = []
    for item in array:
        if "=" in item and "<=" not in item and ">=" not in item and "+" not in item and "-" not in item and "*" not in item and "/" not in item:
            item = item.split("=")
            variables.append([item[0], int(item[1])])
        elif "+" in item:
            first = item.find("=")
            second = item.find("+")
            name = item[first + 1: second]
            value = item[second + 1: len(item)]
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
        elif "-" in item:
            first = item.find("=")
            second = item.find("-")
            name = item[first + 1: second]
            value = item[second + 1: len(item)]
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
        elif "*" in item:
            first = item.find("=")
            second = item.find("*")
            value = item[first + 1: second]
            name = item[second + 1: len(item)]
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
        elif "/" in item:
            first = item.find("=")
            second = item.find("/")
            value = item[first + 1: second]
            name = item[second + 1: len(item)]
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
        elif "submit" in item:
            item = item.replace("submit", "")
            for i in range(len(variables)):
                if variables[i][0] == item:
                    return variables[i][1]
            return "Variable does not exist"




#tree = getTree("a")
depthStack = []
visited = []
#for i in range(len(tree)):
#    visited.append(False)
#print(depthFistSearch(tree, "submita", int(1)))

#print(doInstructions(['a=10', 'b=20', 'a<b?', 'b=b-a', 'submita']))
from Interpreter import interpret
import ImageInterpreter
from SendAndReceive import otherPath

def checkCode(text):
    if text == None:
        return "No text has been entered"
    else:
        accepted = interpret(text)
        if accepted is int:
            if accepted == ImageInterpreter.doInstructions(ImageInterpreter.getInstructions(otherPath)):
                return "The code has been correctly converted"
            else:
                return "The code compiles but the logic is incorrect"
        else:
            return accepted



from classpectGenerator import generateClasspect

MAXCLASSPECTS=16

def generateMessage(isadmin:bool,amount:int,mode:int,farragofiction:bool,minimum:int,maximum:int):
    if not ((1<=amount) and (isadmin or amount<=MAXCLASSPECTS)):
        return "That is not a valid amount of classpects!"
    
    messageBase="Here are your classpects:\n```{}```"
    if amount == 1: messageBase="Here is your classpect:\n```{}```"

    classpects = "\n".join(generateClasspect(mode,farragofiction,minimum,maximum) for _ in range(amount))

    return messageBase.format(classpects)


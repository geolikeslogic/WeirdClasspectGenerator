from classpectGenerator import generateClasspect

MAXCLASSPECTS=16

def generateMessage(amount:int,mode:int,farragofiction:bool):
    if not 1<=amount<=MAXCLASSPECTS:
        return "That is not a valid amount of classpects!"
    
    messageBase="Here are your classpects:\n```{}```"
    if amount == 1: messageBase="Here is your classpect:\n```{}```"

    classpects = "\n".join(generateClasspect(mode,farragofiction) for _ in range(amount))

    return messageBase.format(classpects)


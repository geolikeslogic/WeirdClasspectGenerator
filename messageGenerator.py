from classpectGenerator import generateClasspect
from wordlists import getWordList

MAXCLASSPECTS=16

def generateMessage(interaction,amount:int,mode:int,farragofiction:bool,minimum:int,maximum:int,custom:int,explicit:int,masterclasses:int):
    wordList = getWordList(interaction.guild_id,explicit,custom)
    
    if 1>amount:
        return "That is not a valid amount of classpects!"
    if not (interaction.user.guild_permissions.administrator or amount<=MAXCLASSPECTS):
        return "That is too many classpects for one post!"
    
    messageBase="Here are your classpects:\n```{}```"
    if amount == 1: messageBase="Here is your classpect:\n```{}```"


    classpects = "\n".join(generateClasspect(mode,farragofiction,minimum,maximum,wordList,masterclasses) for _ in range(amount))

    if len(classpects)>2000:return "That message is larger than discord will allow! (2000 characters)"

    return messageBase.format(classpects)


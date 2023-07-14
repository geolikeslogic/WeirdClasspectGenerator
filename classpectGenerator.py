import random
from wordlists import wordList

classFile,aspectFile=open("WordLists/CanonClasses.txt","r"),open("WordLists/CanonAspects.txt","r")
CLASSES,ASPECTS=classFile.readlines(),aspectFile.readlines()
classFile.close()
aspectFile.close()

def formatWord(word):
    return word[0].upper()+word[1:]

def getWord(wordList,minimum=0,maximum=20):
    word=""
    while (not word) or (not minimum<=len(word)<=maximum):
        word = random.choice(wordList)
        if word[-1]=="\n": word = word[:-1]
    return formatWord(word)

def generateClasspect(mode=0,farragofiction=False,minimum=3,maximum=100,wordList=[]):
    Class,Aspect="",""
    CanonClasses,CanonAspects=CLASSES,ASPECTS
    getWordLambda = lambda list: getWord(list,minimum,maximum)
    if not farragofiction:
        CanonClasses,CanonAspects=CanonClasses[:15],CanonAspects[:13]
    match mode:
        case 0:
            Class,Aspect=getWordLambda(wordList),getWordLambda(wordList)
        case 1:
            Class,Aspect=getWordLambda(wordList),getWordLambda(wordList)
            if (Class in ASPECTS) or (Aspect in CLASSES): Class,Aspect=Aspect,Class
        case 2:
            canonPart=random.randint(0,1)==1
            Class,Aspect=getWordLambda(CanonClasses if canonPart==0 else wordList),getWordLambda(CanonAspects if canonPart==1 else wordList)
        case 3:
            Class,Aspect=getWordLambda(CanonClasses),getWordLambda(CanonAspects)
        case 4:
            Class,Aspect=getWordLambda(CanonClasses),getWordLambda(wordList)
        case 5:
            Class,Aspect=getWordLambda(wordList),getWordLambda(CanonAspects)

    return(f"{Class} of {Aspect}")
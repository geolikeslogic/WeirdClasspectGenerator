import random, re

wordsFile = open('wordsNew.txt', 'r') 
words = wordsFile.readlines()
wordsFile.close()

CLASSES,ASPECTS="Lord,Muse,Seer,Mage,Heir,Witch,Sylph,Maid,Bard,Prince,Page,Knight,Rogue,Thief,Smith,Waste,Grace,Guide,Sage,Scout,Scribe".split(","),"Space,Time,Light,Void,Breath,Blood,Mind,Heart,Life,Doom,Hope,Rage,Dreams,Law".split(",")

def formatWord(word):
    return word[0].upper()+word[1:]

def getWord(wordList):
    word=""
    while not word:
        word = random.choice(wordList)
        if word[-1]=="\n": word = word[:-1]
    return formatWord(word)

def generateClasspect(mode=0,farragofiction=False,wordList=words):
    Class,Aspect="",""
    CanonClasses,CanonAspects=CLASSES.copy(),ASPECTS.copy()
    if not farragofiction:
        CanonClasses,CanonAspects=CanonClasses[:13],CanonAspects[:13]
    match mode:
        case 0:
            Class,Aspect=getWord(wordList),getWord(wordList)
        case 1:
            Class,Aspect=getWord(wordList),getWord(wordList)
            if (Class in ASPECTS) or (Aspect in CLASSES): Class,Aspect=Aspect,Class
        case 2:
            canonPart=random.randint(0,1)==1
            Class,Aspect=getWord(CanonClasses if canonPart==0 else wordList),getWord(CanonAspects if canonPart==1 else wordList)
        case 3:
            Class,Aspect=getWord(CanonClasses),getWord(CanonAspects)

    return(f"{Class} of {Aspect}")
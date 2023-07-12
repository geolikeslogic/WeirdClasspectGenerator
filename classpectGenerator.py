import random

wordsFile = open('wordsNew.txt', 'r') 
words = wordsFile.readlines()
wordsFile.close()

CLASSES,ASPECTS="Lord,Muse,Seer,Mage,Heir,Witch,Sylph,Maid,Bard,Prince,Page,Knight,Rogue,Thief,Smith,Waste,Grace,Guide,Sage,Scout,Scribe".split(","),"Space,Time,Light,Void,Breath,Blood,Mind,Heart,Life,Doom,Hope,Rage,Dreams,Law".split(",")

def formatWord(word):
    return word[0].upper()+word[1:]

def getWord(wordList,minimum=0,maximum=20):
    word=""
    while (not word) or (not minimum<=len(word)<=maximum):
        word = random.choice(wordList)
        if word[-1]=="\n": word = word[:-1]
    return formatWord(word)

def generateClasspect(mode=0,farragofiction=False,minimum=3,maximum=100,wordList=words):
    Class,Aspect="",""
    CanonClasses,CanonAspects=CLASSES.copy(),ASPECTS.copy()
    if not farragofiction:
        CanonClasses,CanonAspects=CanonClasses[:13],CanonAspects[:13]
    match mode:
        case 0:
            Class,Aspect=getWord(wordList,minimum,maximum),getWord(wordList,minimum,maximum)
        case 1:
            Class,Aspect=getWord(wordList,minimum,maximum),getWord(wordList,minimum,maximum)
            if (Class in ASPECTS) or (Aspect in CLASSES): Class,Aspect=Aspect,Class
        case 2:
            canonPart=random.randint(0,1)==1
            Class,Aspect=getWord(CanonClasses if canonPart==0 else wordList,minimum,maximum),getWord(CanonAspects if canonPart==1 else wordList,minimum,maximum)
        case 3:
            Class,Aspect=getWord(CanonClasses),getWord(CanonAspects)
        case 4:
            Class,Aspect=getWord(CanonClasses),getWord(wordList,minimum,maximum)
        case 5:
            Class,Aspect=getWord(wordList,minimum,maximum),getWord(CanonAspects)

    return(f"{Class} of {Aspect}")
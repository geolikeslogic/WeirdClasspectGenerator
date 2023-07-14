import os, copy

class wordList:
    main=[]
    explicit=[]
    blacklist=[]
    def __init__(self,file=False):
        self.main=[]
        self.explicit=[]
        self.blacklist=[]
        if not file: return
        for word in file.readlines():
            match word[0]:
                case '~':
                    self.explicit.append(word[1:])
                case '-':
                    self.blacklist.append(word[1:])
                case _:
                    self.main.append(word)

mainWordsFile = open('WordLists/words.txt', 'r') 
mainWords = wordList(mainWordsFile)
mainWordsFile.close()

def subtractList(list1,list2):
    out=[]
    if len(list2)==0:return list1
    for i in list1:
        if not i in list2:
            out.append(i)
    return out

def getFile(serverId):
    exists = os.path.exists("ServerWordLists/"+str(serverId)+".txt")
    out = None
    if not exists: return wordList()
    with open("ServerWordLists/"+str(serverId)+".txt","r") as file:
        out=wordList(file)
    return out

def getWordList(serverId,profanity,custom):
    out = copy.deepcopy(mainWords)
    match custom:
        case 1:
            out=getFile(serverId)
        case 2:
            customWords=getFile(serverId)
            out.main+=customWords.main
            out.explicit+=customWords.explicit
            out.blacklist+=customWords.blacklist
    out.explicit*=profanity
    return subtractList(out.main+out.explicit,out.blacklist)
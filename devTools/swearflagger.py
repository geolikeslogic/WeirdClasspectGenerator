with open("WordLists/flaggedWords.txt","w") as outputFile:
    out=[]
    with open("WordLists/words.txt","r") as wordsFile:
        with open("WordLists/swears.txt","r") as swearsFile:
            swears = swearsFile.readlines()
            for word in wordsFile.readlines():
                if word in swears:
                    word="~"+word
                out.append(word)
    outputFile.writelines(out)
        
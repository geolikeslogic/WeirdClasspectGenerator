output = []
with open('WordLists/words.txt', 'r') as inputFile:
    lines = inputFile.readlines()
    count = len(lines)
    dupes = 0   
    for index in range(count):
        print(f"{index}/{count} checked, {dupes} duplicate entries removed", end="\r", flush=True)
        if not lines[index] in output: 
            output.append(lines[index])
            dupes+=1
            

with open("WordLists/words.txt", "w") as outputFile:
    outputFile.writelines(output)
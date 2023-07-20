def gamestart():
    print("Welcome to Wordle Console Version 1.1,\n Let's start with a five letter word.")
    return
def attemptmsg(attemptcount,maxattemptcount):
    print("Attempt "+str(attemptcount)+"/"+str(maxattemptcount)+":",end="")
    return
def attempterrormsg(msg):
    print(msg)
    return
def printresult(guessword,resultstr):
    for i in range(0,len(resultstr)):
        if resultstr[i]=="0":
            print("["+guessword[i]+"]",end="")
        elif resultstr[i]=="1":
            print("\033[42m["+guessword[i]+"]\033[0m",end="")
        else:
            print("\033[44m["+guessword[i]+"]\033[0m",end="")
    print("")
    return
def gamesummary(iswin,answord):
    if(iswin):
        print("You got that!")
    else:
        print("You've done all attempts, you failed.")
    print("Word:" +answord.get('word') +"\nTranslate:\n"+answord.get('translation')+"\nTag:"+answord.get('tag'))
    return
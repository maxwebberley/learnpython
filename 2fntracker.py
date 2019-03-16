import time
import os
import statistics
from statistics import mode
kills=[]
comments=[]
landed1=[]
amountofgames=0
loop=3
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
print """
  ______         _         _ _         _______             _
 |  ____|       | |       (_) |       |__   __|           | |
 | |__ ___  _ __| |_ _ __  _| |_ ___     | |_ __ __ _  ___| | _____ _ __
 |  __/ _ \| '__| __| '_ \| | __/ _ \    | | '__/ _` |/ __| |/ / _ \ '__|
 | | | (_) | |  | |_| | | | | ||  __/    | | | | (_| | (__|   <  __/ |
 |_|  \___/|_|   \__|_| |_|_|\__\___|    |_|_|  \__,_|\___|_|\_\___|_|

                                 """
print "If you are having issues make sure the number at the start of the .py file is the same as your python version"
def goon():
    goon1=raw_input("Enter to continue")
    if goon1=="":
        return
    else:
        return
goon()
def worstgame():
    cls()
    print ("""
            WORST GAME
            -=-=-=-=-""")
    print ("\n")
    worstkillsis=min(kills)
    worstgameis=kills.index(min(kills))
    worstgameisnumber=worstgameis+1
    worstcommentis=comments[worstgameis]
    landingpointis=landed1[worstgameis]
    print ("Best amount of kills: %d") %worstkillsis
    print ("This was game number: %d") %worstgameisnumber
    print ("Your comment was: %s") %worstcommentis
    print ("You landed at: %s") %landingpointis
    goon()
    addgame()
def bestgame():
    cls()
    print ("""
            BEST GAME
            -=-=-=-=-""")
    print ("\n")
    bestkillsis=max(kills)
    bestgameis=kills.index(max(kills))
    bestgameisnumber=bestgameis+1
    bestcommentis=comments[bestgameis]
    landingpointis=landed1[bestgameis]
    print ("Best amount of kills: %d" %bestkillsis)
    print ("This was game number: %d" %bestgameisnumber)
    print ("Your comment was: %s" %bestcommentis)
    print ("You landed at: %s") %landingpointis
    goon()
    addgame()

def whatnow1():
    whatnow=raw_input("Press enter to continue. Type bg to see your best game. Type wg to see your worst game. > ")
    if whatnow=="":
        addgame()
    else:
        if amountofgames==0:
            print ("You have played zero games.")
            goon()
            addgame()
        if whatnow=="bg":
            bestgame()
        elif whatnow=="wg":
            worstgame()
        else:
            whatnow1()
def stats():
    totalkills = sum(kills)
    kd = 0 if amountofgames == 0 else float(totalkills)/float(amountofgames)
    try:
        mostcommon = statistics.mode(kills)
    except:
        mostcommon = "!!THERE IS NOT 1 MOST COMMON AMOUNT. MORE DATA REQUIRED!!"
    print ("""
             STATISTICS
            -==-=-=-=-=-

Total Kills: %d""") %totalkills
    print ("K/D: %.3f") %kd
    print ("You have played %d games") %amountofgames
    print ("Your most frequent number of kills is %s") %mostcommon
    print ("\n")
    whatnow1()

def kill():
    global amountofgames
    cls()
    print ("-=-=-=-= NEW GAME=-=-=-=- \n \n")
    a=input("Number of kills > (type 'stats' to see stats) ")
    if a=="stats":
        stats()
    elif type(a) is int:
        kills.append(a)
        amountofgames+=1
    else:
        kill()
def landing():
    landed=raw_input("\n Where did you land?. ")
    if type(landed) is int:
        landing()
    else:
        landed1.append(landed)
        addgame()

def comment():
    comment=raw_input("\n What strategy did you use? Hit Enter to skip. ")
    if type(comment) is int:
        comment()
    else:
        comments.append(comment)

        landing()
cls()
print ("""
                        PERSONAL FORTNITE TRACKER
                        -=-=-=-=-=-=-=-=-=-=-=-=-""")
def addgame():
    kill()
    comment()
addgame()

roshamboFile = open(r"day2input.txt", "r")
roshamboList = roshamboFile.readlines()
#rock paper wizard time
tempScore = 0
totalScore = 0
scoresOpp = {"A":1,"B":2,"C":3}
scoresPlayer = {"X":1,"Y":2,"Z":3}
outcomesPlayer = {"X":0,"Y":3,"Z":6}
#wins:
#2-1
#3-2
#1-3
for match in roshamboList:
    #print("adding " + str(scores[match[0]]) + " from a play of " + match[0])
    tempScore += scoresPlayer[match[2]]
    if match[2] in scoresPlayer and match[0] in scoresOpp:
        if scoresPlayer[match[2]] == scoresOpp[match[0]]:
            #print("adding 3 from a draw versus "+ match[2])
            tempScore += 3
        elif (scoresPlayer[match[2]]-scoresOpp[match[0]]) % 3 == 1:
            #print("adding 6 from a win versus "+ match[2])
            tempScore+=6
        else:
            #print("adding 0 from a loss versus "+ match[2])
            pass
    totalScore += tempScore
    tempScore = 0
print("part 1: " + str(totalScore))
tempScore = 0
totalScore = 0
for match in roshamboList:
    tempScore += outcomesPlayer[match[2]]
    if outcomesPlayer[match[2]] == 3:
        tempScore += scoresOpp[match[0]]
    elif outcomesPlayer[match[2]] == 6:
        tempScore += scoresOpp[match[0]]%3+1
    elif scoresOpp[match[0]] == 1:
        tempScore += 3
    else:
        tempScore += scoresOpp[match[0]]-1
    totalScore += tempScore
    tempScore = 0
print("part 2: " + str(totalScore))

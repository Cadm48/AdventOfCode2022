rucksackFile = open(r"day3input.txt", "r")
rucksackList = rucksackFile.readlines()
score = 0
#part 1
'''for sack in rucksackList:
    half = int(len(sack)/2)
    for item in sack[0:half]:
        if item in sack[half:]:
            if ord(item) <= 90:
                score += ord(item)-38
            else:
                score += ord(item)-96
            sack = ""'''
#part 2
found = False
for i in range(0,len(rucksackList),3):
    for item in rucksackList[i]:
        if not found and item in rucksackList[i+1] and item in rucksackList[i+2]:
            if ord(item) <= 90:
                score += ord(item)-38
            else:
                score += ord(item)-96
            found = True
    found = False

print(score)

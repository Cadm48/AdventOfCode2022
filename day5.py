craneFile = open(r"day5input.txt", "r")
craneList = craneFile.readlines()
stacks = [[],["C","F","B","L","D","P","Z","S"],["B","W","H","P","G","V","N"],["G","J","B","W","F"],["S","C","W","L","F","N","J","G"],["H","S","M","P","T","L","J","W"],["S","F","G","W","C","B"],["W","B","Q","M","P","T","H"],["T","W","S","F"],["R","C","N"]]
#stacks = [[],["N","Z"],["D","C","M"],["P"]]
def move(start, end,num):
    #end.insert(0,start.pop(0))
    
    beingCarried = []
    for i in range(num):
        beingCarried.append(start.pop(0))
    return beingCarried + end

for instruction in craneList:
    instructionList = instruction.split(" ")
    #for i in range(int(instructionList[1])):
    stacks[int(instructionList[5])]=move(stacks[int(instructionList[3])],stacks[int(instructionList[5])],int(instructionList[1]))

for j in range(1,len(stacks)):
    print(stacks[j][0])

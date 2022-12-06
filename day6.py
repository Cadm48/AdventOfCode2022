signalFile = open(r"day6input.txt", "r")
signals = signalFile.read()
currentPacket = ["","","",""]
currentMessage = ["","","","","","","","","","","","","",""]
currentCharacter = 0
packetFound = False
packetIndex = 0
messageFound = False
messageIndex = 0
def duplicates(L):
    for num in range(len(L)):
        for letter in L[num+1:]:
            if L[num] == letter:
                return True
    return False
for letter in signals:
    currentCharacter+=1
    currentPacket.append(letter)
    currentPacket.pop(0)
    currentMessage.append(letter)
    currentMessage.pop(0)
    if not duplicates(currentPacket) and currentCharacter >= 4 and not packetFound:
        packetFound = True
        packetIndex = currentCharacter
    if not duplicates(currentMessage) and currentCharacter >= 14 and not messageFound:
        messageFound = True
        messageIndex = currentCharacter
print(packetIndex)
print(messageIndex)
        
    
    

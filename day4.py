campFile = open(r"day4input.txt", "r")
campList = campFile.readlines()
lesser = range(1)
greater = range(1)

consumed = 0
overlapping = 0
for pair in campList:
    interim = pair.split(",")
    
    elf1 = range(int(interim[0].split("-")[0]),int(interim[0].split("-")[1])+1)
    elf2 = range(int(interim[1].split("-")[0]),int(interim[1].split("-")[1])+1)
    if len(elf1) <= len(elf2):
        lesser = elf1
        greater = elf2
    else:
        lesser = elf2
        greater = elf1
    if min(lesser) >= min(greater) and max(lesser) <= max(greater):
        consumed += 1
    found = False
    for section in elf1:
        if section in elf2 and not found:
            overlapping += 1
            found = True
print(consumed)
print(overlapping)

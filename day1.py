calorieFile = open(r"day1input.txt", "r")
calorieList = calorieFile.readlines()
maximum = [0,0,0]
temp = 0
for line in calorieList:
    if line == "\n":
        if temp > min(maximum):
            maximum[maximum.index(min(maximum))] = temp
        temp = 0
    else:
        temp = temp + int(line)
print(sum(maximum))

x = []
invalid = 0

def checkInvalid(number):
    string = str(number)
    if len(string) % 2 == 0 and not (len(string) == 0):
        firsthalf, secondhalf = string[:int(len(string)/2)], string[int(len(string)/2):]
        if firsthalf == secondhalf:
            return number
    return 0
            

with open("Puzzle 3/input.csv") as f:
    for line in f:
        x = line.split(',')

for range in x:
    lowerbound, upperbound = map(int, range.split('-'))
    while (lowerbound <= upperbound):
        invalid += checkInvalid(lowerbound)
        lowerbound += 1

print(invalid)
import re

x = []
input = "Puzzle 4/input.csv"
invalid = 0

# kann man vorher für alle Längen in input berechnen, war mir aber zu doof, war so schon nervig genug

faktoren = {
    1: [],
    2: [1],
    3: [1],
    4: [1, 2],
    5: [1],
    6: [1, 2, 3],
    7: [1],
    8: [1, 2, 4],
    9: [1, 3],
    10: [1, 2, 5],
    11: [1],
    12: [1, 2, 3, 4, 6],
    13: [1],
    14: [1, 7]
}

def checkInvalid(number):
    string = str(number)
    for i in faktoren[len(string)]:
        splitstring = re.findall('.' * i, string)
        if len(set(splitstring)) == 1:
            return number     
    return 0

with open(input) as f:
    for line in f:
        x = line.split(',')

for range in x:
    lowerbound, upperbound = map(int, range.split('-'))
    print("Starting new range:" + range)
    while (lowerbound <= upperbound):
        invalid += checkInvalid(lowerbound)
        lowerbound += 1

print(invalid)
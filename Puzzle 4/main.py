import re
from collections import Counter
from itertools import pairwise
from itertools import combinations

x = []
invalid = 0

# Probably too slow for now

def checkInvalid(number):
    i = 2
    string = str(number)
    digits = dict(Counter(string))
    for a in combinations(digits, len(digits)):
        if a == 1: return 0
    for a,b in pairwise(combinations(digits, len(digits))):
        if a != b:
            return 0
        
    lastcheck = number / 2
    while (i <= lastcheck):
        if len(string) % i == 0:
            splitstring = re.findall('.' * i, string)
            for a, b in pairwise(splitstring):
                if a != b:
                    break
                elif i == len(splitstring):
                    return number      
        i += 1
    return 0

with open("Puzzle 4/input.csv") as f:
    for line in f:
        x = line.split(',')

for range in x:
    lowerbound, upperbound = map(int, range.split('-'))
    print("Starting new range:" + range)
    while (lowerbound <= upperbound):
        invalid += checkInvalid(lowerbound)
        lowerbound += 1

print(invalid)
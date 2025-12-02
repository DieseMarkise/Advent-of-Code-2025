import re
from collections import Counter
from itertools import pairwise
from itertools import combinations
from multiprocessing import Pool

x = []
results = 0

# With parallel processing

def checkInvalid(number):
    i = 2
    string = str(number)

    digits = dict(Counter(string))
    for a,b in pairwise(combinations(digits, len(digits))):
        if a == 1:
            return 0
        if b == 1:
            return 0
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

def process_range(r):
    invalid_count = 0
    lowerbound, upperbound = map(int, r.split('-'))
    while (lowerbound <= upperbound):
        invalid_count += checkInvalid(lowerbound)
        lowerbound += 1
    print("Zahlenbereich" + r + "abgeschlossen")
    return invalid_count

with open("Puzzle 4/input.csv") as f:
    for line in f:
        x = line.split(',')

if __name__ == "__main__":
    with Pool() as pool:
        results = pool.map(process_range, x)

print(results)
inputranges = 'Puzzle 10/inputranges.csv'

ranges = []
filteredRanges = []
k = 0
maxBound = -1
maxLow = -1
freshIngredients = 0

# input sammeln:

with open(inputranges) as f:
    for line in f:
        ranges.append(line.strip('\n'))

# überlappende Zahlenranges zusammenführen und aufsteigend sortieren:

ranges = sorted(ranges, key=lambda r: int(r.split('-')[0]))

for i in range(0, len(ranges), 1):
    lowerbound = ranges[i].split('-')[0]
    upperbound = ranges[i].split('-')[1]
    if int(lowerbound) > int(maxBound):
        for j in range(i, len(ranges) , 1):
            if int(upperbound) < int(ranges[j].split('-')[0]): next
            else:
                if int(upperbound) <= int(ranges[j].split('-')[1]):
                    upperbound = ranges[j].split('-')[1]
                    i = j
                    maxBound = upperbound
        filteredRanges.append(lowerbound + '-' + upperbound)

for s in filteredRanges:
    freshIngredients += int(s.split('-')[1]) - int(s.split('-')[0]) + 1

print(freshIngredients)
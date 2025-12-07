input = 'Puzzle 14/input.csv'
x = []

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

numberArray = []

for line in x:
    tempList = []
    for c in line:
        if c == '.': tempList.append(0)
        if c == 'S': tempList.append(1)
        if c == '^': tempList.append(-1)
    numberArray.append(tempList)

for i in range(1, len(numberArray), 1):
    for c in range(0, len(numberArray[i]), 1):
        if numberArray[i-1][c] > 0:
            if numberArray[i][c] >= 0:
                numberArray[i][c] += numberArray[i-1][c]
            if numberArray[i][c] == -1:
                numberArray[i][c-1] += numberArray[i-1][c]
                numberArray[i][c+1] += numberArray[i-1][c]

counter = sum(numberArray[-1])

print(counter)
input = 'Puzzle 12/input.csv'

problems = []
flippedProblems = []
presumArray = []
fullSum = 0

i = 0

def multiplyList(list):
    sum = 1
    for i in list:
        sum = sum * int(i)
    return sum

with open(input) as f:
    for line in f:
        problems.append(line.strip('\n'))

for column in range(0, len(problems[0]), 1): 
    presum = ''
    if problems[-1][column] != ' ': operator = problems[-1][column]
    for line in range(0, len(problems)-1, 1):
        presum = presum + problems[line][column]
    presum = presum.replace(' ', '')
    if presum == "" or column == len(problems[0]) - 1:
        if column == len(problems[0]) - 1 and presum != "": presumArray.append(presum)
        if operator == '+':
            fullSum += sum(map(int, presumArray))
        if operator == '*':
            fullSum += multiplyList(presumArray)
        presumArray = []
    else: presumArray.append(presum)

print(fullSum)


input = 'Puzzle 11/input.csv'

problems = []
flippedProblems = []

sum = 0

i = 0

with open(input) as f:
    for line in f:
        problems.append(line.strip('\n'))

while True:
    row = ""
    if i > len(problems[0].split()) - 1: break
    for j in problems:
        row = row + ' ' + j.split()[i]
    flippedProblems.append(row)
    i += 1

for problem in flippedProblems:
    operator = problem.split()[-1]
    if operator == '+': equals = 0
    if operator == '*': equals = 1
    for j in range(0, len(problem.split())- 1, 1):
        if operator == '+': equals += int(problem.split()[j])
        if operator == '*': equals *= int(problem.split()[j])
    sum += equals

print(sum)


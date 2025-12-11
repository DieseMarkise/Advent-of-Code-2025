input = 'Puzzle 21/input.csv'

x = []

end = 'out'
start = 'you'
sumOfPaths = 0

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

data = []

for i in range(len(x)):
    data.append([x[i].split(':')[0], x[i].split(':')[1].split()[:]])

print(data)

def searchStep(machine, visitedMachines = None):
    if visitedMachines == None:
        visitedMachines = set()
    if machine[0] in visitedMachines:
        return 0
    if end in machine[1]:
        return 1
    visitedMachines = visitedMachines.copy()
    visitedMachines.add(machine[0])
    count = 0
    for nextMachine in data:
        if nextMachine[0] in machine[1]:
            count += searchStep(nextMachine, visitedMachines)
    
    return count


for machine in data:
    if start == machine[0]:
        sumOfPaths += searchStep(machine)
        
print(sumOfPaths)
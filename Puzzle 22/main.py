input = 'Puzzle 22/input.csv'

x = []

end = 'out'
start = 'svr'
sumOfPaths = 0

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

data = []

for i in range(len(x)):
    data.append([x[i].split(':')[0], x[i].split(':')[1].split()[:]])

memo = {}

                           
def searchStep(machine, visitedMachines = None):
    if visitedMachines == None:
        visitedMachines = set()
    
    hasFFT = 'fft' in visitedMachines
    hasDAC = 'dac' in visitedMachines


    key = (machine[0], hasFFT, hasDAC)
    if key in memo:
        return memo[key]
    
    if machine[0] in visitedMachines:
        return 0
    
    visitedMachines = visitedMachines.copy()
    visitedMachines.add(machine[0])

    if end in machine[1]:
        if 'fft' in visitedMachines and 'dac' in visitedMachines:
            print('found path')
            result = 1
        else:
            result = 0
        memo[key] = result
        return result
        
    count = 0
    for nextMachine in data:
        if nextMachine[0] in machine[1]:
            count += searchStep(nextMachine, visitedMachines)
    
    memo[key] = count
    return count

for machine in data:
    if start == machine[0]:
        sumOfPaths += searchStep(machine)
        
print(sumOfPaths)
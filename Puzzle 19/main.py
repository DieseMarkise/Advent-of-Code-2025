input = 'Puzzle 19/input.csv'

x = []

sum = 0

searchDepth = 200

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

def lightMap(c):
    if c == '#': return 1
    # elif c == '.': return 0
    else: return 0

def flip(arrangement, operation):
    outputArrangement = []
    for i in range(0, len(arrangement), 1):
        if i in operation: outputArrangement.append(1 - arrangement[i])
        else: outputArrangement.append(arrangement[i])
    return outputArrangement


def iterateOperationsStopOnGoal(start_arrangement, operations, d, goal):

    def applyOperation(arrangement, operations, op_idx):
        return flip(arrangement, operations[op_idx])

    # Startknoten
    current = [(start_arrangement, [])]

    for depth in range(1, d+1):
        next_level = []

        for arr, path in current:
            for op_idx in range(len(operations)):

                new_arr = applyOperation(arr, operations, op_idx)
                new_path = path + [op_idx]

                # Ziel erreicht → SOFORT abbrechen
                if new_arr == goal:
                    return (depth, new_arr, new_path)

                next_level.append((new_arr, new_path))

        current = next_level

    # nichts gefunden
    return None


for machines in x:
    goal = list(map(lightMap, machines.split()[0][1:-1]))
    startingArrangement = [0] * len(goal)
    # lights = list(map(int, machines.split()[-1].lstrip('{').rstrip('}').split(',')[:]))
    strOperations = machines.split()[1:-1]
    operations = []
    for operation in strOperations:
        operations.append(list(map(int,operation.lstrip('(').rstrip(')').split(',')[:])))
    
    result = iterateOperationsStopOnGoal(startingArrangement, operations, searchDepth, goal)

    if result is None:
        print("Kein Pfad innerhalb der Tiefe gefunden.")
    else:
        depth, arrangement, path = result
        sum += depth
        print("Gefunden auf Tiefe:", depth)
        print("Arrangement:", arrangement)
        print("Pfad:", path)

print('Summe der Operationen:', sum)

    # print(lights)
    # print(operations)
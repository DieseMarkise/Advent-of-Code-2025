input = 'Puzzle 20/input.csv'

x = []

sum_depth = 0

searchDepth = 200

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

def lightMap(c):
    if c == '#': return 1
    # elif c == '.': return 0
    else: return 0

def increment(arrangement, operation):
    outputArrangement = []
    for i in range(0, len(arrangement), 1):
        if i in operation: outputArrangement.append(arrangement[i] + 1)
        else: outputArrangement.append(arrangement[i])
    return outputArrangement


def iterateOperationsStopOnGoalVisited(start_arrangement, operations, d, goal):
    m = 0
    def applyOperation(arrangement, operations, op_idx):
        return increment(arrangement, operations[op_idx])

    current = [(start_arrangement, [])]
    visited = set()
    visited.add(tuple(start_arrangement))

    for depth in range(1, d+1):
        next_level = []

        for arr, path in current:
            for op_idx in range(len(operations)):

                new_arr = applyOperation(arr, operations, op_idx)
                new_path = path + [op_idx]
                m = (m + 1) % 200000
                if m == 0:
                    print(new_arr, sum(new_arr))

                if any(new_arr[i] > goal[i] for i in range(len(goal))):
                    continue

                arr_tuple = tuple(new_arr)
                if arr_tuple in visited:
                    continue
                visited.add(arr_tuple)

                if new_arr == goal:
                    return (depth, new_arr, new_path)

                next_level.append((new_arr, new_path))

        if not next_level:
            return None

        current = next_level

    return None


for machines in x:
    goal = list(map(lightMap, machines.split()[0][1:-1]))
    startingArrangement = [0] * len(goal)
    lights = list(map(int, machines.split()[-1].lstrip('{').rstrip('}').split(',')[:]))
    strOperations = machines.split()[1:-1]
    operations = []
    for operation in strOperations:
        operations.append(list(map(int,operation.lstrip('(').rstrip(')').split(',')[:])))
    operations.sort(reverse=True, key=sum)
    result = iterateOperationsStopOnGoalVisited(startingArrangement, operations, searchDepth, lights)

    if result is None:
        print("Kein Pfad innerhalb der Tiefe gefunden.")
    else:
        depth, arrangement, path = result
        sum_depth += depth
        print("Gefunden auf Tiefe:", depth)
        print("Arrangement:", arrangement)
        print("Pfad:", path)

print('Summe der Operationen:', sum)
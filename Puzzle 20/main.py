import pulp

input = 'Puzzle 20/input.csv'

x = []

sum_presses = 0

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

def lightMap(c):
    if c == '#': return 1
    else: return 0

def solve_operations_ilp(goal, operations):
    problem = pulp.LpProblem("OpSolve", pulp.LpMinimize)

    k = len(operations)
    d = len(goal)

    c = [pulp.LpVariable(f"c_{j}", lowBound=0, cat='Integer') for j in range(k)]

    problem += pulp.lpSum(c)

    for i in range(d):
        problem += pulp.lpSum(c[j] * operations[j][i] for j in range(k)) == goal[i]

    status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[status] != 'Optimal':
        return None

    return [int(v.value()) for v in c]


for machines in x:
    lights = list(map(int, machines.split()[-1].lstrip('{').rstrip('}').split(',')[:]))
    strOperations = machines.split()[1:-1]
    operations_raw = []
    operations = []
    for operation in strOperations:
        operations_raw.append(list(map(int, operation.lstrip('(').rstrip(')').split(','))))
    for operation in operations_raw:
        vector = [0] * len(lights)
        for index in operation:
            vector[index] = 1
        operations.append(vector)
    operations.sort(reverse=True, key=sum)

    result = solve_operations_ilp(lights, operations)
    print(result)
    sum_presses += sum(result)
    


print('Summe der Operationen:', sum_presses)
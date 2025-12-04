input = "Puzzle 7/input.csv"

x = []
reachability = 3
reachable = 0
hit = '@'

def isHit(c):
    return c == hit

def isMiss(c):
    return not isHit(c)

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

for i in range(0, len(x), 1):
    for k in range(0, len(x[i]), 1):
        neighbours = 8
        if isHit(x[i][k]):
            # print(str(i) + "," + str(k) + " ist ein Hit")
            # column above
            if(i > 0):
                if (k > 0):
                    if isMiss(x[i-1][k-1]): neighbours -= 1
                else: neighbours -= 1
                if isMiss(x[i-1][k]): neighbours -= 1
                if (k < len(x[i-1]) - 1):
                    if isMiss(x[i-1][k+1]): neighbours -= 1
                else: neighbours -= 1
            else: neighbours -= 3
            # column below
            if(i < len(x) - 1):
                if (k > 0):
                    if isMiss(x[i+1][k-1]): neighbours -= 1
                else: neighbours -= 1
                if isMiss(x[i+1][k]): neighbours -= 1
                if (k < len(x[i+1]) - 1):
                    if isMiss(x[i+1][k+1]): neighbours -= 1
                else: neighbours -= 1
            else: neighbours -= 3
            # same column
            if (k > 0):
                if isMiss(x[i][k-1]): neighbours -= 1
            else: neighbours -= 1
            if (k < len(x[i]) - 1):
                if isMiss(x[i][k+1]): neighbours -= 1
            else: neighbours -= 1

            if neighbours <= reachability: reachable += 1

print(reachable)
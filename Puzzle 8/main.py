input = "Puzzle 8/input.csv"

x = []
reachability = 3
removable = 0
reachable = 0
hit = '@'
miss = '.'

def isHit(c):
    return c == hit

def isMiss(c):
    return not isHit(c)

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))
while True:
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

                if neighbours <= reachability:
                    removable += 1
                    x[i] = x[i][:k] + '.' + x[i][k + 1:]

    if removable == 0: break
    print(str(removable) + "konnten entfernt werden")
    reachable += removable
    removable = 0

print(reachable)
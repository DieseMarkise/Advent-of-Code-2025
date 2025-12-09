input = 'Puzzle 15/input.csv'

x = []
connections = 1000

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

distMatrix = []

for i in range(0, len(x), 1):
    tempArray = []
    for j in range(0, i, 1):
        tempArray.append(0)
    for j in range(i+1, len(x), 1):
        p1 = x[i].split(',')
        p2 = x[j].split(',')
        dist = (int(p1[0]) - int(p2[0])) ** 2 + (int(p1[1]) - int(p2[1])) ** 2 + (int(p1[2]) - int(p2[2])) ** 2
        tempArray.append(dist)
    distMatrix.append(tempArray)

listOfDistances = []

for i in range(0, len(distMatrix), 1):
    for j in range(i+1, len(distMatrix[i]), 1):
        tuple = [distMatrix[i][j], i, j + 1]
        listOfDistances.append(tuple)

listOfDistances.sort(key=lambda listOfDistances: listOfDistances[0])

networks = []

for i in listOfDistances[:connections]:
    added = False
    p1 = i[1]
    p2 = i[2]
    for j in networks:
        if (p1 in j): 
            if not (p2 in j):
                j.append(p2)
                added = True
        elif (p2 in j): 
            if not (p1 in j):
                j.append(p1)
                added = True
    if added: next
    else: networks.append([p1, p2])

networks.sort(reverse = True, key=len)

changed = True
while changed:
    changed = False
    merged = []

    for net in networks:
        net = set(net)
        for other in merged:
            if not net.isdisjoint(other):
                other |= net
                changed = True
                break
        else:
            merged.append(net)

    networks = merged


print(networks)

sum = len(networks[0]) * len(networks[1]) * len(networks[2])

print(sum)
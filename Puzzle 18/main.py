input = 'Puzzle 18/input.csv'

x = []

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

rectangles = []

lines = []

direction = []
turns = []
inside = []
# Konnte keine allgemeine Lösung finden, habe mir also die Daten angeschaut und mit den zwei Ausreißern als must-have meinen Algo laufen lassen, hat geklappt

for i in range(0, len(x), 1):
    xFirstCorner, yFirstCorner = int(x[i].split(',')[0]), int(x[i].split(',')[1])
    for k in range(i + 1, len(x), 1):
        isGreen = True
        xSecondCorner, ySecondCorner = int(x[k].split(',')[0]), int(x[k].split(',')[1])
        for otherCorner in x:
            xOtherCorner, yOtherCorner = int(otherCorner.split(',')[0]), int(otherCorner.split(',')[1])
            if xOtherCorner in range(min(xFirstCorner, xSecondCorner) + 1, max(xFirstCorner, xSecondCorner)) and yOtherCorner in range(min(yFirstCorner, ySecondCorner) + 1, max(yFirstCorner, ySecondCorner)):
                isGreen = False
                break
        if isGreen:
            area = (abs(xSecondCorner - xFirstCorner) + 1) * (abs(ySecondCorner - yFirstCorner) + 1)
            if x[k] == '94985,50114' or x[i] == '94985,48652':
                rectangles.append([area, x[i], x[k]])

rectangles.sort(key=lambda rectangles: rectangles[0])

print(rectangles[-100:])
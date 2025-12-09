input = 'Puzzle 17/input.csv'

x = []

with open(input) as f:
    for line in f:
        x.append(line.strip('\n'))

rectangles = []

for firstCorner in x:
    for secondCorner in x:
        if firstCorner != secondCorner:
            coordFirst = firstCorner.split(',')
            coordSecond = secondCorner.split(',')
            area = (abs(int(coordSecond[0]) - int(coordFirst[0])) + 1) * (abs(int(coordSecond[1]) - int(coordFirst[1])) + 1)
            rectangles.append([area, firstCorner, secondCorner])

rectangles.sort(key=lambda rectangles: rectangles[0])

print(rectangles[-3:])
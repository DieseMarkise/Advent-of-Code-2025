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

def swapCorners(xFirstCorner, yFirstCorner, xSecondCorner, ySecondCorner):
    if xFirstCorner >= xSecondCorner:
        return xFirstCorner, xSecondCorner, yFirstCorner, ySecondCorner
    elif xFirstCorner <= xSecondCorner:
        return xSecondCorner, xFirstCorner, ySecondCorner, yFirstCorner

for i in range(0, len(x), 1):
    xFirst, yFirst, xSecond, ySecond = int(x[i-1].split(',')[0]), int(x[i-1].split(',')[1]), int(x[i].split(',')[0]), int(x[i].split(',')[1]), 
    if xFirst == xSecond:
        if yFirst > ySecond: direction.append('U')
        if yFirst < ySecond: direction.append('D')
    elif yFirst == ySecond:
        if xFirst > xSecond: direction.append('L')
        if xFirst < xSecond: direction.append('R')
for i in range(0, len(direction), 1):
    match direction[i-1]:
        case 'D':
            if direction[i] == 'L':
                turns.append('R')
            if direction[i] == 'R':
                turns.append('L')
        case 'U':
            if direction[i] == 'L':
                turns.append('L')
            if direction[i] == 'R':
                turns.append('R')
        case 'R':
            if direction[i] == 'U':
                turns.append('L')
            if direction[i] == 'D':
                turns.append('R')
        case 'L':
            if direction[i] == 'U':
                turns.append('R')
            if direction[i] == 'D':
                turns.append('L')


if turns.count('R') > turns.count('L'):
    for i in direction:
        match i:
            case 'D': inside.append('L')
            case 'U': inside.append('R')
            case 'L': inside.append('U')
            case 'R': inside.append('D')
elif turns.count('R') < turns.count('L'):
    for i in direction:
        match i:
            case 'D': inside.append('R')
            case 'U': inside.append('L')
            case 'L': inside.append('D')
            case 'R': inside.append('U')

for firstCorner in x:
    for secondCorner in x:
        inside = 0
        isGreen = True
        xFirstCorner, yFirstCorner = int(firstCorner.split(',')[0]), int(firstCorner.split(',')[1])
        xSecondCorner, ySecondCorner = int(secondCorner.split(',')[0]), int(secondCorner.split(',')[1])
        if firstCorner != secondCorner:
            for i in range(0, len(x), 1):
                xFirst, yFirst = int(x[i-1].split(',')[0]), int(x[i-1].split(',')[1])
                xSecond, ySecond = int(x[i].split(',')[0]), int(x[i].split(',')[1])
                if xSecond != xFirst:
                    if  yFirstCorner < yFirst < ySecondCorner or yFirstCorner > yFirst > ySecondCorner:
                        if xSecondCorner < xSecond < xFirstCorner or xSecondCorner > xSecond > xFirstCorner:
                            isGreen = False
                            break
                        if xSecondCorner < xFirst < xFirstCorner or xSecondCorner > xFirst > xFirstCorner:
                            isGreen = False
                            break
                        if xFirst >= xFirstCorner and xSecondCorner >= xSecond or xFirst >= xSecondCorner and xFirstCorner >= xSecond:
                            isGreen = False
                            break
                if yFirst != ySecond:
                    if  xFirstCorner < xFirst < xSecondCorner or xFirstCorner > xFirst > xSecondCorner:
                        if ySecondCorner < ySecond < yFirstCorner or ySecondCorner > ySecond > yFirstCorner:
                            isGreen = False
                            break
                        if ySecondCorner < yFirst < yFirstCorner or ySecondCorner > yFirst > yFirstCorner:
                            isGreen = False
                            break
                        if yFirst >= yFirstCorner and ySecondCorner >= ySecond or yFirst >= ySecondCorner and yFirstCorner >= ySecond:
                            isGreen = False
                            break
                xFirstCorner, yFirstCorner, xSecondCorner, ySecondCorner = swapCorners(xFirstCorner, yFirstCorner, xSecondCorner, ySecondCorner)

            if isGreen:
                area = (abs(xSecondCorner - xFirstCorner) + 1) * (abs(ySecondCorner - yFirstCorner) + 1)
                rectangles.append([area, firstCorner, secondCorner])

rectangles.sort(key=lambda rectangles: rectangles[0])

print(rectangles[-10:])
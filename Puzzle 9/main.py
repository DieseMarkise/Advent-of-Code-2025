inputnumbers = 'Puzzle 9/inputnumbers.csv'
inputranges = 'Puzzle 9/inputranges.csv'

numbers = []
ranges = []
k = 0
freshIngredients = 0

# input sammeln:

with open(inputnumbers) as f:
    for line in f:
        numbers.append(line.strip('\n'))

with open(inputranges) as f:
    for line in f:
        ranges.append(line.strip('\n'))

# Zahlenranges aufsteigend sortieren:

ranges = sorted(ranges, key=lambda r: int(r.split('-')[1]))

# Duplikate der Zahlen filtern und aufsteigend sortieren:

numbers = sorted(set(numbers), key=lambda n: int(n))


for n in numbers:
    for f in set(ranges):
        if int(n) <= int(f.split('-')[1]) and int(n) >= int(f.split('-')[0]):
            freshIngredients += 1
            break

print(freshIngredients)


list = []

number = 50

count = 0

with open ('Puzzle1 /input.csv') as file:
    for line in file:
        match line[0]:
            case 'R':
                number = (number + int(line[1:])) % 100
            case 'L':
                number = (number - int(line[1:])) % 100
            case _:
                print("Kein R oder L erkannt")
        if number == 0:
            count += 1

print(count)
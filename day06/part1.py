grid = open(0).read().splitlines()

result = 0
numbers = []
for r, row in enumerate(grid):
    cols = row.split()
    if r == len(grid) - 1:
        for c, op in enumerate(cols):
            acc = 1 if op == "*" else 0
            for i in range(len(numbers)):
                if op == "*":
                    acc *= numbers[i][c]
                else:
                    acc += numbers[i][c]
            result += acc
    else:
        numbers.append([int(x) for x in cols])

print(result)

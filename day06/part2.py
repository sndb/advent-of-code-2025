grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 0
numbers = []
for c in range(cols - 1, -1, -1):
    curr = 0
    for r in range(rows):
        x = grid[r][c]
        if x.isnumeric():
            curr *= 10
            curr += int(x)

        if r == rows - 1 and curr != 0:
            numbers.append(curr)
            curr = 0

        if x in "*+":
            acc = 1 if x == "*" else 0

            for n in numbers:
                if x == "*":
                    acc *= n
                else:
                    acc += n

            numbers = []
            result += acc

print(result)

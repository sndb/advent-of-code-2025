grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 0
seen = set()
queue = [(0, grid[0].index("S"))]
while queue:
    r, c = queue.pop()
    if (r, c) in seen or r >= rows or c < 0 or c >= cols:
        continue
    seen.add((r, c))

    if grid[r][c] == "^":
        result += 1
        queue.append((r, c - 1))
        queue.append((r, c + 1))
    else:
        queue.append((r + 1, c))

print(result)

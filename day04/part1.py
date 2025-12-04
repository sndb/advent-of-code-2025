grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 0

for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x != "@":
            continue

        adj = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == dc == 0:
                    continue

                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    adj += 1

        if adj < 4:
            result += 1

print(result)

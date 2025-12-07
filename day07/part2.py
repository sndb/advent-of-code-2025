import functools

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

@functools.cache
def timelines(r, c):
    if r == rows:
        return 1

    if c < 0 or c >= cols:
        return 0

    if grid[r][c] == "^":
        return timelines(r, c - 1) + timelines(r, c + 1)

    return timelines(r + 1, c)

print(timelines(0, grid[0].index("S")))

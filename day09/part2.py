points = []
for line in open(0).read().splitlines():
    c, r = map(int, line.split(","))
    points.append((r, c))

path = set()
walls = set()
prev_dir = None
wr, wc = 0, 1 # hardcoded wall offset
for i in range(len(points)):
    r1, c1 = points[i]
    r2, c2 = points[(i + 1) % len(points)]

    curr_dir = (r2 - r1, c2 - c1)

    if prev_dir:
        pr, pc = prev_dir
        nr, nc = curr_dir
        if pc > 0 and nr > 0 or pr > 0 and nc < 0 or pc < 0 and nr < 0 or pr < 0 and nc > 0:
            wr, wc = wc, -wr
        else:
            wr, wc = -wc, wr

    if r1 == r2:
        cmin, cmax = sorted([c1, c2])
        for c in range(cmin, cmax + 1):
            path.add((r1, c))
            walls.add((r1 + wr, c + wc))
    else:
        rmin, rmax = sorted([r1, r2])
        for r in range(rmin, rmax + 1):
            path.add((r, c1))
            walls.add((r + wr, c1 + wc))

    prev_dir = curr_dir

walls = sorted(walls - path)

def find_row(r):
    lo, hi = 0, len(walls) - 1
    while lo <= hi:
        mi = (lo + hi) // 2
        wr, _ = walls[mi]
        if wr < r:
            lo = mi + 1
        else:
            hi = mi - 1
    return lo

def wall_inside(r1, c1, r2, c2):
    for i in range(find_row(r1), find_row(r2 + 1)):
        _, wc = walls[i]
        if c1 <= wc <= c2:
            return True
    return False

result = 0
for i, (r1, c1) in enumerate(points):
    for r2, c2 in points[i + 1 :]:
        rmin, rmax = sorted([r1, r2])
        cmin, cmax = sorted([c1, c2])
        if not wall_inside(rmin, cmin, rmax, cmax):
            area = (rmax - rmin + 1) * (cmax - cmin + 1)
            result = max(result, area)

print(result)

points = [(*map(int, line.split(",")),) for line in open(0).read().splitlines()]

result = 0
for i, (x1, y1) in enumerate(points):
    for x2, y2 in points[i + 1 :]:
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        result = max(result, area)

print(result)

import math

boxes = [(*map(int, line.split(",")),) for line in open(0).read().splitlines()]

dists = []
for i, b1 in enumerate(boxes):
    for b2 in boxes[i + 1 :]:
        dist = math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(b1, b2)))
        dists.append((dist, b1, b2))

dists.sort()

circuits = {b: b for b in boxes}

def parent(b):
    p = circuits[b]
    if p == b:
        return b

    circuits[b] = parent(p)
    return circuits[b]

for _, b1, b2 in dists:
    p1 = parent(b1)
    p2 = parent(b2)
    if p1 != p2:
        circuits[p2] = p1
        r1, r2 = b1, b2

print(r1[0] * r2[0])

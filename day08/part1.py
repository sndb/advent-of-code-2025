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

for i, (_, b1, b2) in enumerate(dists):
    if i == 1000:
        break

    p1 = parent(b1)
    p2 = parent(b2)
    if p1 != p2:
        circuits[p2] = p1

counts = {b: 0 for b in boxes}
for b in boxes:
    counts[parent(b)] += 1

print(math.prod(sorted(counts.values())[-3:]))

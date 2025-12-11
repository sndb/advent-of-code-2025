graph = {}
for line in open(0).read().splitlines():
    fields = line.split()
    graph[fields[0][:-1]] = fields[1:]

def paths(a, b):
    return a == b or sum(paths(n, b) for n in graph[a])

print(paths("you", "out"))

from functools import cache

graph = {}
for line in open(0).read().splitlines():
    fields = line.split()
    graph[fields[0][:-1]] = fields[1:]

@cache
def paths(a, b, fft, dac):
    if a == b:
        return fft and dac

    return sum(paths(n, b, fft or a == "fft", dac or a == "dac") for n in graph[a])

print(paths("svr", "out", False, False))

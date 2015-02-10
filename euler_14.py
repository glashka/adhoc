paths = {}
paths[1] = 1

def next_step(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    return n

for i in xrange(1, 1000000):
    if i % 1000 == 0:
        print i, len(paths)
    path = list()
    path.append(i)
    while i not in paths.keys():
        i = next_step(i)
        path.append(i)
    for j in xrange(len(path)):
        paths[path[j]] = len(path) - 1 - j + paths[i]

print max(paths, key=paths.get)
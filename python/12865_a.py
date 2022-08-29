items,weights = map(int, input().split())

thing = [[0,0]]
d = [[0]*(weights+1) for _ in range(items+1)]

for i in range(items):
    thing.append(list(map(int, input().split())))


for i in range(1, items+1):
    for j in range(1, weights+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(thing)
print(d)
print(d[items][weights])
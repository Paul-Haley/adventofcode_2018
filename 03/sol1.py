map = dict()
with open('input') as f:
    for line in f:
        s = line.split(' ')
        tl = (int(s[2].split(',')[0]), int(s[2].split(',')[1].split(':')[0]))
        size = (int(s[-1].split('x')[0]), int(s[-1].split('x')[1]))
        claim = int(s[0][1:])
        for i in range(tl[0], tl[0] + size[0]):
            for j in range(tl[1], tl[1] + size[1]):
                if not map.get((i,j)):
                    map[(i,j)] = set()
                map[(i,j)].add(claim)

overlaps = 0
for cell in map:
    if len(map[cell]) > 1:
        overlaps = overlaps + 1
print(overlaps)

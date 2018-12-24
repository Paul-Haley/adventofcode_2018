combos = dict()
with open('input') as f:
    for line in f:
        d = dict()
        d.setdefault(0)
        for c in line:
            d[c] = d.get(c, 0) + 1
        combos[line] = d

for i in combos:
    for j in combos:
        singleDiff = False
        for k in range(0, len(i)):
            if i[k] == j[k]:
                continue
            elif i[k] != j[k] and not singleDiff:
                singleDiff = True
            else:
                break
        else:
            if singleDiff:
                out = ""
                for k in range(0, len(i)):
                    if i[k] == j[k]:
                        out = out + i[k]
                print(out)

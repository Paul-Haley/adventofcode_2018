with open('input') as f:
    two = 0
    three = 0
    for line in f:
        d = dict()
        d.setdefault(0)
        for c in line:
            d[c] = d.get(c, 0) + 1
        twoseen = False
        threeseen = False
        for e in d:
            if d[e] == 2:
                twoseen = True
            elif d[e] == 3:
                threeseen = True
        two = two + twoseen
        three = three + threeseen
    print(two*three)
            


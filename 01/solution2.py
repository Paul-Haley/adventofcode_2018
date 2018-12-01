t = 0
notDone = True
seen = set()
while (notDone):
    with open('input') as f:
        for i in f:
            n = int(i[1:])
            if i[0] == '+':
                t = t + n
            else:
                t = t - n
            if t in seen:
                print(t)
                notDone = False
                break
            seen.add(t)


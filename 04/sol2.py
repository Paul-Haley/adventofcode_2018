guards = dict()
dates = list()
with open('input') as f:
    for line in f:
        s = line.split(' ')
        action = ''
        if s[2] == 'falls':
            action = 'f'
        elif s[3][0] == '#':
            action = s[3][1:]
        else:
            action = 'w'
        dates.append((line[1:17], action))

dates.sort()

guard = -1
f = 0
w = 59
te = lambda e: int(e[0].split(' ')[1].split(':')[1])
for e in dates:
    if e[1] == 'f':
        f = te(e)
    elif e[1] == 'w':
        w = te(e)
        for i in range(f, w):
            guards[guard][i] = guards[guard][i] + 1
    else: #new guard
        guard = int(e[1])
        if not guards.get(guard):
            guards[guard] = [0] * 60

x = (0, 0, 0)
for g in guards:
    times = guards[g]
    for i in range(len(times)):
        if times[i] > x[2]:
            x = (g, i, times[i])
print(x[0]*x[1])

t = 0
with open('input') as f:
    for i in f:
        n = int(i[1:])
        if i[0] == '+':
            t = t + n
        else:
            t = t - n
print(t)


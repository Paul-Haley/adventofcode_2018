with open('input') as f:
    s = f.read().split(' ')
    players = int(s[0])
    final = int(s[6])*100

marble = 0
current = 0
circle = [0, None]
player = 0
scores = [0] * players

for marble in range(1, final + 1):
    #if marble == final:
    #    marble = marble * 100
    if marble % 23 == 0:
        i = (current - 7)%(len(circle) - 1)
        scores[player] = scores[player] + marble + circle.pop(i)
        current = i % (len(circle) -1)
    else:
        current = (current + 2)%(len(circle)-1)
        if current == len(circle) - 1:
            circle.append(marble)
            current = current + 1
        else:
            circle.insert(current, marble) 


    player = (player + 1) % players

print(max(scores))


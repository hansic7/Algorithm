N = int(input())

cards = []

for i in range(N):
    cards.append(int(input()))

cards.sort()
result = cards[0]
befo = 1
now = 1
for i in range(1, len(cards)):
    if cards[i] == cards[i-1]:
        now += 1
    else:
        if befo < now:
            befo = now
            result = cards[i-1]
        now = 1

if befo < now:
        befo = now
        result = cards[i-1] 

print(result)
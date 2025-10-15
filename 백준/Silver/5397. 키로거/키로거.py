n = int(input())

for _ in range(n):
    key_log = str(input())

    left, right = [], []

    for i in key_log:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
        
    for i in range(len(right)-1, -1, -1):
        left.append(right[i])

    print(''.join(left))
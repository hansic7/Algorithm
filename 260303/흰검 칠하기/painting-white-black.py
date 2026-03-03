n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)


arr = [0] * 200001
xi = 100000
b, w, g = 0,0,0

for i in range(n):
    if dir[i] == 'R':
        tmp_i = xi + x[i]
        for j in range(xi, tmp_i, 1):
            if 0 < arr[j] < 3:
                w-=1
                b+=1
            elif arr[j] == 0:
                b += 1
            elif arr[j] == 3:
                w-=1
                g+=1
            arr[j] += 1
        xi = tmp_i - 1
    else:
        tmp_i = xi - x[i]
        for j in range(xi, tmp_i, -1):
            if 0 < arr[j] < 3:
                w+=1
                b-=1
            elif arr[j] == 0:
                w += 1
            elif arr[j] == 3:
                b -= 1
                g += 1
            arr[j] += 1
        xi = tmp_i + 1

print(w,b,g)
        

# Please write your code here.

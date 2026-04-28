n = int(input())
dict = {}
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        dict[k] = v
    elif cmd == "remove":
        dict.pop(k)
    else:
        if k in dict:
            print(dict[k])
        else:
            print("None")

# Please write your code here.

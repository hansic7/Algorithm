s = input()

answer = []
flag = 0

def reverse(tmp):
    for j in range(len(tmp) - 1, -1, -1):
        answer.append(tmp[j])

tmp = []
for i in s:
    if i == " ":
        reverse(tmp)
        tmp = []
        answer.append(i)

    elif i == "<":
        if tmp:
            reverse(tmp)
        tmp = []
        flag = 1
        answer.append(i)

    elif i == ">":
        flag = 0
        answer.append(i)

    elif flag == 1:
        answer.append(i)

    elif flag == 0:
        tmp.append(i)

if tmp:
    reverse(tmp)
    
print("".join(answer))

n, m = map(int, input().split())
arr1 = [0]
arr2 = [0]

# Process robot A's movements
for _ in range(n):
    time, direction = input().split()
    for _ in range(int(time)):
        if direction == 'R':
            arr1.append(arr1[-1] + 1)
        else:
            arr1.append(arr1[-1] - 1)

# Process robot B's movements
for _ in range(m):
    time, direction = input().split()
    for _ in range(int(time)):
        if direction == 'R':
            arr2.append(arr2[-1] + 1)
        else:
            arr2.append(arr2[-1] - 1)


a_last = len(arr1)
b_last = len(arr2)
diff_place = False
cnt = 0
for i in range(max(a_last, b_last)):
    a1 = (-1 if i >= a_last else i)
    b1 = (-1 if i >= b_last else i)
    if arr1[a1] == arr2[b1]: 
        if diff_place:
            # print("a1 = ", a1, " arr1[a1] =", arr1[a1], " b1 =", b1, " arr2[b1]=", arr2[b1])
            cnt += 1
            diff_place = False
    else:
        diff_place = True

# print(arr1)
# print(arr2)
print(cnt) 

# Please write your code here.
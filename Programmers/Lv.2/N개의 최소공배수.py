
def solution(arr):
    gcm = [arr[0]]
    for i in range(1, len(arr)):
        gcm.append(arr[i])
        while max(gcm) % min(gcm) != 0:
            gcm.sort()
            gcm[1] = gcm[1] // gcm[0]
            



    return






arr = [2, 6, 8, 14]
print(solution(arr))







'''  처음썻던 방법
prime = [2]
for i in range(3,140):
    flag = 0
    for j in range(2, (i//2+1)):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        prime.append(i)
print(prime)


def solution(arr):
    answer = 1
    last = []
    lenn = len(arr)
    for i in prime:
        flag = []
        for j in range(lenn):
            if arr[j] % i == 0:
                flag.append(j)
        if len(flag) >= 2:
            for j in flag:
                arr[j] = arr[j] // i
            last.append(i)
    print(arr)
    print(last)
    for i in arr:
        answer *= i
    for i in last:
        answer *= i
    return answer
'''
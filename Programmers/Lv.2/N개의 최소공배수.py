
def least(a, b):
    A, B = a, b
    # print(f"A,B = {A}, {B}")
    print(f"a = {a}, b = {b}")
    while b > 0:
        r = a%b
        a = b
        b = r
        print(f"a = {a}, b = {b}")
        
    GCD = a # 최대공약수
    return A * B // GCD

# arr에서 앞 2개씩 접근하면서 최소공배수 갱신
def solution(arr):
    arr.sort()
    temp = arr[0]
    for i in range(0, len(arr)-1):
        print(f"i = {i}")
        temp = least(temp, arr[i+1])
        print()
    return temp






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
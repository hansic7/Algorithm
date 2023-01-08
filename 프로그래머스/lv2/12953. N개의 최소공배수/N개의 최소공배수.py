
def least(a, b):
    A, B = a, b
    # print(f"A,B = {A}, {B}")
    # print(f"a = {a}, b = {b}")
    while b > 0:
        r = a%b
        a = b
        b = r
        # print(f"a = {a}, b = {b}")
        
    GCD = a # 최대공약수
    return A * B // GCD

# arr에서 앞 2개씩 접근하면서 최소공배수 갱신
def solution(arr):
    arr.sort()
    temp = arr[0]
    for i in range(0, len(arr)-1):
        # print(f"i = {i}")
        temp = least(temp, arr[i+1])
        # print()
    return temp
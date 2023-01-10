
def solution(n):
    answer = 0
    m = n
    while m > 1:
        m = m//2
        if m % 2 == 1:
            answer += 1

    if n % 2 == 1:
        answer += 1

    return answer
print(solution(6))




#  처음엔 DP로 풀었는데 시간초과 남 패턴 찾아서 효율적으로 가야되는듯?
def solution(n):
    dd = [0] * (n+1)
    dd[1] = 1

    for i in range(2, n+1):
        if i % 2 == 0 and dd[i//2] != 0:
            dd[i] = dd[(i//2)]
        else:
            dd[i] = dd[(i-1)] + 1
    # print(f"i = {i}, {dd}")
    return (dd[n])
# 
print(solution(5000))
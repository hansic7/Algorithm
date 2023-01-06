
def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            if sum > n:
                break
    return answer

print(solution(15))







'''
내가 만들었던 오답코드

def solution(n):
    answer = 1
    dd = [1]
    for i in range(2, (n//2)+2):
        dd.append(dd[-1] + i)
    # print(dd)
    for i in range(n//2+1):
        for j in range(i):
            # print(f"i = {dd[i]}, j = {dd[j]}, dd[i] - dd[j] = {dd[i] - dd[j]}")
            if dd[i] == n:
                answer += 1
                break
            elif dd[i] - dd[j] < n:
                break
            if dd[i] - dd[j] == n:
                answer += 1
                break
    return answer

print(solution(15))
'''
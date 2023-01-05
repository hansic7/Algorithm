def solution(n):
    dd = [0,1,1]
    
    if n >= 3:
        for i in range(3, n+1):
            dd.append(dd[i-1] + dd[i-2])

    answer = dd[n] % 1234567
    return answer
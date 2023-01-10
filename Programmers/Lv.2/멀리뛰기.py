

def solution(n):
    dd = [0] * (n+1)
    dd[0], dd[1] = 1, 2
    for i in range(2, n+1): ## n+1 까지 돌리지 않으면 n=1일 경우 에러뜰듯?
        dd[i] = dd[i-1] + dd[i-2]
    print(dd)

    return (dd[n-1] % 1234567) ##모듈러 안해서 틀림. 문제를 잘 읽자

print(solution(20))


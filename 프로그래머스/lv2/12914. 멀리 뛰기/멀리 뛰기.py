def solution(n):
    dd = [0] * (n+1)
    dd[0], dd[1] = 1, 2
    for i in range(2, n+1):
        dd[i] = dd[i-1] + dd[i-2]

    return (dd[n-1] % 1234567)

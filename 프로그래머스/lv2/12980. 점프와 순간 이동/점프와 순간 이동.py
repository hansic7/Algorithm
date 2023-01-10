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
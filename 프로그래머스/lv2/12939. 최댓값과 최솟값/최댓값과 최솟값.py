def solution(s):
    s = list(map(int, s.split()))
    answer = str(min(s))
    answer += ' '
    answer += str(max(s))
    return answer
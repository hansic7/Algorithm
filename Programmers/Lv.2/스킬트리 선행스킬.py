from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        s = deque(skill)
        flag =1
        for j in i:
            if j in s :
                if s and s[0] != j:
                    flag = 0
                    break
                else:
                    s.popleft()
        if flag ==1:
            answer += 1
    return answer

a = "CBD"
b = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(a,b))
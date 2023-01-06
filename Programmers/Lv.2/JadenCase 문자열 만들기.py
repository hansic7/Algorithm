

s = "3people unFollowed me"
# s[0].capitalize()

def solution(s):
    words = s.split(' ')
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return(' '.join(words))



print(solution(s))
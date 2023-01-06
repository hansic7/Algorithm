


'''문제에서 가장 중요한거는 26칸짜리 체크테이블을 만든 후 단어를 넣어 다른 사람이 말한것을 
또 언급하나 중복체크를 해주는것이다'''

def solution(n, words):
    pp = [0] * n
    words_check = [[] for i in range(26)]   ### 체크테이블 만들어서 단어 넣어주기
    pp[0] = 1
    words_check[ord(words[0][0]) - ord('a')].append(words[0])

    for i in range(1, len(words)):
        if (words[i][0] == words[i-1][-1] and
            not words[i] in words_check[ord(words[i][0]) - ord('a')]) :
            pp[i % n] += 1
            words_check[ord(words[i][0]) - ord('a')].append(words[i])
            # print(pp)
            # print(words_check)
            continue

        else:
            return([i % n +1, pp[i % n] +1])
    return[0,0]


words = 		["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(2, words))
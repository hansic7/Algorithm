def solution(n, words):
    pp = [0] * n
    words_check = [[] for i in range(26)]
    pp[0] = 1
    words_check[ord(words[0][0]) - ord('a')].append(words[0])

    for i in range(1, len(words)):
        if (words[i][0] == words[i-1][-1] and
            not words[i] in words_check[ord(words[i][0]) - ord('a')]) :
            pp[i % n] += 1
            words_check[ord(words[i][0]) - ord('a')].append(words[i])
            continue

        else:
            return([i % n +1, pp[i % n]+1])
    return[0,0]
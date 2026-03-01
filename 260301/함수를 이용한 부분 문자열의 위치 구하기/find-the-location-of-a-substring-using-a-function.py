text = input()
pattern = input()

def bu():
    for i in range(len(text)):
        if text[i] == pattern[0]:
            tmp_i = i
            for j in range(1, len(pattern)):
                tmp_i += 1
                if tmp_i >= len(text):
                    break
                if text[tmp_i] != pattern[j]:
                    break
                if j == len(pattern) - 1:
                    return i
    return -1

print(bu())
                

# Please write your code here.
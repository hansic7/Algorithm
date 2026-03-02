word1 = input()
word2 = input()


def check():
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False
    return True
    
    

if len(word1) != len(word2):
    print('No')
else:
    word1 = ''.join(sorted(word1))
    word2 = ''.join(sorted(word2))

    if check():
        print('Yes')
    else:
        print('No')

# Please write your code here.

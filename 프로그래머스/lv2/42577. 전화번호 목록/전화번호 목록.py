def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x))
    
    numbers = {}
    cnts = {}
    
    cnts[len(phone_book[0])] = 1
    numbers[phone_book[0]] = 1
    
    bookLen = len(phone_book)
    if bookLen > 1:
        for i in range(1, bookLen):
            for j in cnts:
                if phone_book[i][0:j] in numbers:
                    return False
                    exit()
            numbers[phone_book[i]] = 1
            cnts[len(phone_book[i])] = 1
    
    return answer
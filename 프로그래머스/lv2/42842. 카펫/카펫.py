def solution(brown, yellow):
    
    for i in range(1,brown):
        if yellow % i == 0:
            y = yellow // i
            x = i
            if ((y+2)*2) + ((x+2)*2) - 4 == brown:
                return[y+2,x+2]

    return False
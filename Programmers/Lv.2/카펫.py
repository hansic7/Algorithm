def solution(brown, yellow):
    
    for i in range(1,yellow):
        if yellow % i == 0:
            y = yellow // i
            x = i
            if ((y+2)*2) + ((x+2)*2) - 4 == brown:
                return[y+2,x+2]
    return False

print(solution(10,2))



''' 망한코드 -- x와 y가 1씩 순서대로 증가하기에 [7,6]은 찾을수있는데 [8,6]같은건 못 찾음

def solution(brown, yellow):
    x,y = 1,1
    while True:
        if ((x*2) + ((y-2)*2) == brown) and ((x-2) * (y-2) == yellow):
            break
        x = x+1
        print(x,y)

        if ((x*2) + ((y-2)*2) == brown) and ((x-2) * (y-2) == yellow):
            break
        y = y + 1
        print(x,y)
    return [x,y]

print(solution(24,24))
'''

def solution(brown, yellow):
    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            yellow_x = int(yellow/i)
            yellow_y = i
            if yellow_x*2 + yellow_y*2 + 4 == brown :            
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return sorted(answer, reverse = True)
    
    return answer
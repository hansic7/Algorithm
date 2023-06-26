
def solution(land):
    answer = 0

    arr = [[0]*4 for i in range(len(land))]
    
    for i in range(4):
        arr[0][i] = land[0][i]

    for i in range(len(land)):
        for j in range(4):
            temp = []
            for z in range(4):
                if z != j: temp.append(arr[i-1][z])
            arr[i][j] = land[i][j] + max(temp)
        
    return max(arr[len(land)-1])

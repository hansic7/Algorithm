def solution(n, costs):
    answer = 0
    ans_cnt = 0
    
    uf = [i for i in range(n+1)]
    
    def find(x):
        if uf[x] == x:
            return x
        uf[x] = find(uf[x])
        return uf[x]
    
    def union(x, y):
        a,b = find(x), find(y)
        if a != b:
            uf[a] = b
            return 1
        
        return 0
    
    costs.sort(key = lambda x : x[2])
    
    for x,y,w in costs:
        if union(x,y):
            answer += w
            ans_cnt += 1
        if ans_cnt == n -1:
            break
            
    return answer

def dfs(cnt, k, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= k:
            k -= dungeons[i][1]
            visited[i] = True
            dfs(cnt+1, k, dungeons, visited)
            k += dungeons[i][1]
            visited[i] = False
        

def solution(k, dungeons):
    global answer
    answer = 0
    
    visited = [False] * len(dungeons)
    dfs(0, k, dungeons, visited)
    
    return answer



        
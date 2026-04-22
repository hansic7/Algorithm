import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    
    # reach[i][j] = i에서 j로 도달 가능 (i < j 관계 앎)
    reach = [[False] * (N + 1) for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        reach[a][b] = True  # a < b
    
    # Floyd-Warshall
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    
    # 각 노드별 비교 불가 쌍 수 계산
    for i in range(1, N + 1):
        count = 0
        for j in range(1, N + 1):
            if i == j:
                continue
            # i→j도 j→i도 없으면 비교 불가
            if not reach[i][j] and not reach[j][i]:
                count += 1
        print(count)

solve()
import sys
input = sys.stdin.readline
# N, M = map(int,input().split())
N,M = 3,6
ddd = ['1 1 1 2',
'2 1 2 2',
'1 1 1 3',
'2 3 3 1',
'1 3 1 2',
'1 3 2 1']


#불끈 곳에 방문하면 방문처리 1하고
#대기실에 넣어둠
light =[ [0]*(N+2) for _ in range(N+2) ] #불이 켜졌는지 여부
light[1][1] =1

visited= [[0]*(N+2) for _ in range(N+2) ]
visited[1][1]=1
for i in range(N+2):
    visited[i][0]=1
    visited[i][N+1]=1
    visited[0][i]=1
    visited[N+1][i]=1

print(f"this is visisted = {visited}")

    

Map = [ [ [] for i in range(N+2)] for j in range(N+2)] #스위치

for i in range(M):
    a,b,c,d=map(int,ddd[i].split())
    Map[a][b].append((c,d))


cnt = 1 #시작방
wait = set()
que= [ (1,1)]

while que:
    nq = []

    for r,c in que:
        for lr, lc in Map[r][c]:
            if light[lr][lc]:
                continue
            cnt+=1
            light[lr][lc]=1
            if (lr,lc) in wait:
                nq.append( (lr,lc) )
                #visited는 이미 되어있음
        for nr,nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if visited[nr][nc]==0:
                visited[nr][nc]=1
                if light[nr][nc]:
                    nq.append( (nr,nc))
                else:
                    wait.add( (nr,nc) )

    que = nq
print(cnt)

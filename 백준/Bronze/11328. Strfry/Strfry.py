N = int(input())

for i in range(N):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    
    nn = len(a)
    if nn != len(b):
        print("Impossible")
    else:
        answer = "Possible"
        for i in range(nn):
            if a[i] != b[i]:
                answer = "Impossible"
                break
        print(answer)
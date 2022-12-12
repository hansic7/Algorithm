dd = ["26 40 83",
"49 60 57",
"13 89 99"]
dd=['71 39 44',
'32 83 55',
'51 37 63',
'89 29 100',
'83 58 11',
'65 13 15',
'47 25 29',
'60 66 19'
]



# N = int(input())
N = 8


color = []
for i in range(N):
    # color.append(list(map(int, input().split())))
    color.append(list(map(int, dd[i].split())))

for i in range(1, N):
    color[i][0] += min(color[i-1][1], color[i-1][2])
    color[i][1] += min(color[i-1][0], color[i-1][2])
    color[i][2] += min(color[i-1][0], color[i-1][1])

print(min(color[N-1][0], color[N-1][1], color[N-1][2]))

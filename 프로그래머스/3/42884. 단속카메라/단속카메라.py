def solution(routes):
    answer = 1
    routes.sort(key = lambda x : x[0])

    camera = routes[0][1]
    for i in range(1, len(routes)):
        nx, ny = routes[i][0], routes[i][1]
        if ny < camera:
            camera = ny
        elif camera < nx:
            camera = ny
            answer += 1
    
    return answer
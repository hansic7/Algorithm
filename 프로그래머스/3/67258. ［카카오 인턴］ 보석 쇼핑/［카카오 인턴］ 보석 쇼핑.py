def solution(gems):
    total = len(set(gems))          # 전체 보석 종류 수
    cnt = {}                        # 현재 윈도우 안 보석별 개수
    left = 0
    best = (0, len(gems) - 1)       # 최악의 경우 = 전체 구간

    for right, g in enumerate(gems):
        cnt[g] = cnt.get(g, 0) + 1

        # 왼쪽 보석이 윈도우 안에 2개 이상이면 버려도 종류 수는 그대로
        while cnt[gems[left]] > 1:
            cnt[gems[left]] -= 1
            left += 1

        if len(cnt) == total and right - left < best[1] - best[0]:
            best = (left, right)

    return [best[0] + 1, best[1] + 1]
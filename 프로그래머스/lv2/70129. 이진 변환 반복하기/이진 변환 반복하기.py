def solution(s):
    answer = [0, 0]  # 이진 변환의 횟수와 제거된 0의 개수를 저장할 변수

    while s != "1":  # s가 "1"이 될 때까지 반복
        # 0 제거
        removed_zeros = s.count("0")  # 제거된 0의 개수
        s = s.replace("0", "")

        # 이진 변환
        s = bin(len(s))[2:]  # 길이를 2진법으로 변환한 문자열
        answer[0] += 1  # 이진 변환 횟수 증가
        answer[1] += removed_zeros  # 제거된 0의 개수 누적

    return answer
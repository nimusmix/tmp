import sys
sys.stdin = open('input (5).txt')

for tc in range(1, 11):
    N = int(input())

    mags = [list(map(int, input().split())) for _ in range(100)]
    mags = list(map(list, list(zip(*mags))))                 # 리스트 가로로 뒤집기
    cnt = 0

    for i in mags:
        while 0 in i:                                        # 리스트 내의 0 모두 제거
            i.remove(0)
        i.insert(0, 0)                                       # indexError 방지하기 위해
        i.append(0)                                          # 리스트의 시작과 끝에 0 추가

        for j in range(1, len(i)-1):                         # 0이 제거된 리스트를 순회하며
            if i[j] == 2 and i[j-1] == 1:                    # 2의 왼쪽에 1이 있으면 count
                cnt += 1

    print(f'#{tc} {cnt}')
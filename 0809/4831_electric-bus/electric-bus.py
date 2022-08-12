import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for cnt in range(1, T+1):
    K, N, M = map(int, input().split())
    stop = [0] * N
    charge = list(map(int, input().split()))
    c_cnt = 0

    for j in charge:
        stop[j] = 1

    print(stop)

    i = 0

    while i < N - K:                 # 충전기가 필요한 최대 범위
        for j in range(K, 0, -1):    # 해당 위치에서부터 갈 수 있는 가장 먼 위치부터 충전소 확인
            if stop[i + j] == 1:     # 충전소를 찾으면 해당 인덱스를 불러오고 개수 1 증가
                i = i + j
                c_cnt += 1
                break
            elif j == 1:             # 충전소를 끝까지 못 찾았을 경우, while문 탈출과 cnt를 0으로 초기화
                i = N
                c_cnt = 0

    print(f'#{cnt} {c_cnt}')
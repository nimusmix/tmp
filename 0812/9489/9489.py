import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if pic[i][j] == 1:
                cnt += 1
                if cnt > maxV:
                    maxV = cnt
            else:
                cnt = 0


    for i in range(M):
        cnt = 0
        for j in range(N):
            if pic[j][i] == 1:
                cnt += 1
                if cnt > maxV:
                    maxV = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxV}')
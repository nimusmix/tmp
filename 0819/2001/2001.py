import sys
sys.stdin = open('input (3).txt')

T = int(input())

def my_sum(li):
    result = 0
    for s in li:
        result += s
    return result

for tc in range(1, T+1):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for j in range(N-M+1):
        for i in range(N-M+1):
            temp = 0
            for m in range(M):
                temp += my_sum(flies[i+m][j:j+M])
            if temp > maxV:
                maxV = temp

    print(f'#{tc} {maxV}')
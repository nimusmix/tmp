import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    sum_li = []

    for i in range(N-M+1):
        sum_li.append(sum(li[i:i+M]))

    print(f'#{tc} {max(sum_li)-min(sum_li)}')
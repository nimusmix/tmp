import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for k in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    max = min = li[0]

    for i in range(1, N):
        if li[i] > max:
            max = li[i]
        elif li[i] < min:
            min = li[i]

    print(f'#{k} {max-min}')
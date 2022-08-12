import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))

    for _ in range(N):
        li[li.index(max(li))] -= 1
        li[li.index(min(li))] += 1

    print(f'#{tc} {max(li) - min(li)}')
T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    n = a.count(b)
    print(f'#{tc} {len(a)-len(b)*n+n}')
T = int(input())

def binary(x):
    s = 1
    e = P
    cnt = 0

    while 1:
        c = int((s + e) // 2)

        if c == x:
            return cnt
        elif c > x:
            e = c
        elif c < x:
            s = c

        cnt += 1

for tc in range(1, T+1):
    P, PA, PB = map(int, input().split())

    if binary(PA) < binary(PB): print(f'#{tc} A')
    elif binary(PA) == binary(PB): print(f'#{tc} 0')
    else: print(f'#{tc} B')


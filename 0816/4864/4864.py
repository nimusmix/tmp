T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()

    print(f'#{tc} 1' if N in M else f'#{tc} 0')
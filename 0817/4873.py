T = int(input())

for tc in range(1, T+1):
    word = input()
    top = -1
    stack = [0] * 1001

    for i in word:
        if stack[top] != i:
            top += 1
            stack[top] = i
        else:
            stack.pop(top)
            top -= 1

    print(f'#{tc} {top+1}')
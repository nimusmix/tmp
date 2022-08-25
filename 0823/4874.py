T = int(input())

for tc in range(1, T+1):
    code = list(input().split())
    stack = []
    operator = ['*', '/', '+', '-']

    print(f'#{tc}', end=' ')
    for i in code:
        try:
            if i.isdigit():
                stack.append(i)
            elif i in operator:
                tmp1 = int(stack.pop())
                tmp2 = int(stack.pop())
                if i == '*': stack.append(tmp2 * tmp1)
                elif i == '/': stack.append(int(tmp2 / tmp1))
                elif i == '+': stack.append(tmp2 + tmp1)
                elif i == '-': stack.append(tmp2 - tmp1)
            elif i == '.' and len(stack) == 1:
                print(stack.pop())
            else:
                print('error')
        except:
            print('error')
            break
T = int(input())

for tc in range(1, T+1):
    some = input()

    top = -1
    stack = []

    for i in range(len(some)):
        if some[i] == '(' or some[i] == '{':
            stack.append(some[i])
            top += 1
        elif some[i] == ')' or some[i] == '}':
            top -= 1
            try:
                temp = stack.pop()
                if some[i] == ')' and temp != '(':
                    print(f'#{tc} 0')
                    break
                elif some[i] == '}' and temp != '{':
                    print(f'#{tc} 0')
                    break
            except:
                print(f'#{tc} 0')
                break
    else:
        if top != -1:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')
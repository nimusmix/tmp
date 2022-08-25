T = int(input())

rank = {'*': [2, 2], '/': [2, 2], '+': [1, 1], '-': [1, 1], '(': [0, 3]}

for tc in range(1, T+1):
    word = input()
    stack = []
    digit = list(map(str, range(10)))
    temp = ''

    print(f'#{tc}', end=' ')
    for i in word:
        if i in digit:
            print(i, end='')
        elif i == ')':
            while temp != '(':
                temp = stack.pop()
                if temp != '(':
                    print(temp, end='')
        else:
            if stack == [] or rank[i][1] > rank[stack[-1]][0]:
                stack.append(i)
            else:
                while stack != [] and rank[i][1] <= rank[stack[-1]][0]:
                    temp = stack.pop()
                    print(temp, end='')
                stack.append(i)

    while len(stack) > 0:
        temp = stack.pop()
        print(temp, end='')

    print()
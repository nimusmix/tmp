def itoa(x):
    word = ''
    minus = False

    if x == 0:
        return chr(48)

    if x < 0:
        minus = True
        x = x * -1

    while x > 0:
        word = chr(48 + x % 10) + word
        x //= 10

    if minus:
        word = '-' + word

    return word

tc = 0

while 1:
    tc += 1
    N = int(input())

    print(f'#{tc} {itoa(N)} {type(itoa(N))}')
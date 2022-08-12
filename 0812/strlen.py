a = list(input())

def strlen(x):
    tmp = 0
    num = 0

    while 1:
        if tmp == '\\' and x[num] == '0':
            return num-1
        tmp = x[num]
        num += 1

print(strlen(a))
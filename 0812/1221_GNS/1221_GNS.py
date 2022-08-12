import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
GNS_li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, T+1):
    tc, N = input().split()
    li = list(map(str, input().split()))

    for i in range(int(N)):
        for jdx, j in enumerate(GNS_li):
            if li[i] == j:
                li[i] = jdx

    li.sort()

    for i in range(int(N)):
        for jdx, j in enumerate(GNS_li):
            if li[i] == jdx:
                li[i] = j

    print(tc)
    print(*li)
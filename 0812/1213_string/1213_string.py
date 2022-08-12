import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF-8')

def cnt_bruteforce(pattern, source):
    cnt = 0
    for idx in range(len(source) - len(pattern) + 1):
        for j in range(len(pattern)):
            if source[idx + j] != pattern[j]:
                break
        else:
            cnt += 1
    else:
        return cnt

for _ in range(10):
    tc = int(input())

    pattern = input()
    source = input()

    print(f'#{tc} {cnt_bruteforce(pattern, source)}')
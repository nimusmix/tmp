T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input()))
    cnt_dict = {}

    for i in range(10, -1, -1):
        cnt_dict[i] = li.count(i)

    print(f'#{tc} {max(cnt_dict, key=cnt_dict.get)} {max(cnt_dict.values())}')
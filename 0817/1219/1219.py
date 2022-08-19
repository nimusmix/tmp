import sys
sys.stdin = open('input (1).txt')

def dfs(x):
    visited[x] = 1
    for i in adjList[x]:
        if visited[i] == 0:
            dfs(i)

for _ in range(10):
    tc, n = map(int, input().split())
    pair_list = list(map(int, input().split()))
    adjList = [[] for _ in range(100)]
    visited = [0] * 100

    for i in range(0, n*2, 2):
        adjList[pair_list[i]].append(pair_list[i+1])

    dfs(0)
    print(f'#{tc} {visited[99]}')

import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

def dfs(x):
    visited[x] = 1
    for i in adjList[x]:
        if visited[i] == 0:
            dfs(i)

for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V+1
    adjList = [[] for _ in range(N)]
    visited = [0] * N

    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)

    S, G = map(int, input().split())

    dfs(S)
    print(f'#{tc} {visited[G]}')